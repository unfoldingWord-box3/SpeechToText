import os
import json
import re
import whisper_timestamped as whisper
import string
import inflect
import argparse
import requests
from fuzzywuzzy import process
from pydub import AudioSegment


p = inflect.engine()


def transcribe_file(mp3_path, transcription_path, lang):
    model = whisper.load_model(name="tiny", download_root="./.cache")
    audio = whisper.load_audio(mp3_path)
    print(f"Transcribing {mp3_path}...")
    transcription = whisper.transcribe(model, audio, language=lang)
    with open(transcription_path, "w") as json_file:
        json.dump(transcription, json_file, indent=4)
    print("Done transcribing.")


def flatten_transcription(transcription_path, flattened_path):
    # Read the JSON file
    with open(transcription_path, 'r') as f:
        data = json.load(f)

    resultArr = []
    total = 0
    id = 0
    for i, segment in enumerate(data["segments"]):
        for j, word in enumerate(segment["words"]):
            id += 1
            text = word["text"].lower().strip(string.punctuation)
            if text.isdigit():
                text = p.number_to_words(text)
            word["text"] = text
            word["segment"] = segment["id"]
            word["story-index"] = id
            word["segment-index"] = j + 1 
            resultArr.append(word)
            total += 1
    with open(flattened_path, "w") as json_file:
        json.dump(resultArr, json_file, indent=4)


def tokenize_story_frames(md_path, story_data_path):
    # Read the Markdown file
    with open(md_path, 'r') as f:
        text = f.read()

    text = text.replace('’', "'")

    paragraphs = re.split(r'!\[.*\]\(.*\)\n', text)

    result = {
        "text": text,
        "segments": []
    }
    resultArr = []
    word_positions = {}
    for i, paragraph in enumerate(paragraphs):
        paragraph = paragraph.strip()
        words_in_paragraph = re.findall(r"\b[\w'-]+\b", paragraph)
        segment = {
            "text": paragraph.strip(),
            "words": []
        }
        for j, word in enumerate(words_in_paragraph, 1):
            if word not in word_positions:
                word_positions[word] = []
            word_positions[word].append(j)
            text = word.lower().strip(string.punctuation)
            if text.isdigit():
                text = p.number_to_words(text)
            wordObj = {"text": text, "occurrence": len(word_positions[word]), "frame": i}
            segment["words"].append(wordObj)
            resultArr.append(wordObj)
        result["segments"].append(segment)

    # with open(story_data_path, "w") as json_file:
    #     json.dump(result, json_file, indent=4)
    with open(story_data_path, "w") as json_file:
        json.dump(resultArr, json_file, indent=4) 
   

def fuzzy_merge_objects(story_list_path, transcription_list_path, merged_list_path):
    with open(story_list_path, 'r') as f:
        list1 = json.load(f)
    with open(transcription_list_path, 'r') as f:
        list2 = json.load(f)

    # Extract the "text" properties
    texts1 = [obj['text'] for obj in list1]
    texts2 = [obj['text'] for obj in list2]

    # Fuzzy match the texts
    merged_texts = []
    missed_texts = []

    list2index = 0
    for list1index, item1 in enumerate(list1):
        if list2index >= len(list2):
            merged_texts.append({"frame": item1, "mp3": None})
            missed_texts.append({"frame": item1, "mp3": None})
            break
        upperIndex = list2index+(10 if list2index == 0 else 5)
        highest = process.extractOne(item1, list2[list2index:upperIndex], lambda x: x["text"])
        if highest[1] > 80:  # Adjust the threshold as needed
            for list2subindex, item2 in  enumerate(list2[list2index:upperIndex]):
                if item2 == highest[0]:
                    list2index = list2index + list2subindex + 1
                    merged_texts.append({"frame": item1, "mp3": item2})
                    break
                else:
                    merged_texts.append({"frame": None, "mp3": item2})
                    missed_texts.append({"frame": None, "mp3": item2})
        else:
            merged_texts.append({"frame": item1, "mp3": None})
            missed_texts.append({"frame": item1, "mp3": None})
        if not merged_texts[-1]["frame"]:
            print(f"We have a problem merging {story_list_path}:{list1index} with {transcription_list_path}:{list2index} - ")
            print(item1)
            print("in")
            print(list2[list2index:upperIndex])
            exit(1)

    with open(merged_list_path, "w") as json_file:
        json.dump(merged_texts, json_file, indent=4)
    with open(merged_list_path.replace("merged", "missed"), "w") as json_file:
        json.dump(missed_texts, json_file, indent=4)

def get_frame_times(story_data_path, merged_list_path, frame_times_path):
    with open(story_data_path, 'r') as f:
        story_data = json.load(f)
    with open(merged_list_path, 'r') as f:
        merged_data = json.load(f)

    last_frame = story_data[-1]["frame"]
    frame_times = {}

    for frameNum in range(0, last_frame + 1):
        started = False
        ended = False
        frameStartMp3 = None
        nextFrameStartMp3 = None
        for i, mergedObj in enumerate(merged_data):
            if mergedObj["frame"] and mergedObj["frame"]["frame"] == frameNum:
                started = True
            if started and not frameStartMp3 and mergedObj["mp3"]:
                frameStartMp3 = mergedObj["mp3"]
            if i == len(merged_data) - 1 or (started and mergedObj["frame"] and mergedObj["frame"]["frame"] > frameNum):
                ended = True
            if mergedObj["mp3"]:
                nextFrameStartMp3 = mergedObj["mp3"]
            if ended and mergedObj["mp3"]:
                break
        if not nextFrameStartMp3:
            print(f"FAILED TO FIND A START MP3 OBJECT FOR FRAME {frameNum} in {merged_list_path}!!!!")
            exit(1)
        current_frame_start = round(frameStartMp3["start"] - 0.2, 2)            
        if frameNum != last_frame:
            current_frame_end = round(nextFrameStartMp3["start"] - 0.03, 2)
        else:
            current_frame_end = round(nextFrameStartMp3["end"], 2)
        duration = round(current_frame_end - current_frame_start, 2)
        frame_times[str(frameNum).zfill(2)] = {"frame": frameNum, "start": current_frame_start, "duration": duration, "end": current_frame_end}

    with open(frame_times_path, "w") as json_file:
        json.dump(frame_times, json_file, indent=4)

    return frame_times
    

def cut_mp3(file_path, start_time, end_time, output_path):
    # Load audio file
    audio = AudioSegment.from_mp3(file_path)

    # Convert time to milliseconds
    start_time = start_time * 1000
    end_time = end_time * 1000

    # Extract segment
    audio_segment = audio[start_time:end_time]

    # Export segment
    audio_segment.export(output_path, format="mp3")


def download_files(lang, version, story, output_dir):
    # Download the MP3 file
    mp3_path = os.path.join(output_dir, f"{lang}_obs_{version}_{story}_128kbps.mp3")
    if not os.path.exists(mp3_path):
        mp3_url = f"https://cdn.door43.org/{lang}/obs/{version}/128kbps/{lang}_obs_{story}_128kbps.mp3"
        response = requests.get(mp3_url)
        with open(mp3_path, "wb") as f:
            f.write(response.content)
        print(f"Downloaded {mp3_url} to {mp3_path}")

    md_path = os.path.join(output_dir, f"{lang}_obs_{version}_{story}.md")
    if not os.path.exists(md_path):
        md_url = f"https://git.door43.org/unfoldingWord/{lang}_obs/raw/tag/{version}/content/{story}.md"
        response = requests.get(md_url)
        with open(md_path, "w") as f:
            f.write(response.text)
        print(f"Downloaded {md_url} to {md_path}")
    return (mp3_path, md_path)


def process_story(lang, version, story, frame, output_dir):
    story_padded = str(story).zfill(2)
    frame_padded = str(frame).zfill(2)

    mp3_path, md_path = download_files(lang, version, story_padded, output_dir)
    clip_path = mp3_path.replace("_128kbps.mp3", f"-{frame_padded}_128kbps.mp3")
    if os.path.exists(clip_path):
        print(f"Clip already exists at {clip_path}")
        exit(0)
    transcription_path = os.path.join(output_dir, f"{lang}_obs_{version}_{story_padded}.transcription.json")
    flattened_path = os.path.join(output_dir, f"{lang}_obs_{version}_{story_padded}.transcription.flattened.json")
    story_data_path = os.path.join(output_dir, f"{lang}_obs_{version}_{story_padded}.story.frame.json")
    merged_list_path = os.path.join(output_dir, f"{lang}_obs_{version}_{story_padded}.merged.json")
    frame_times_path = os.path.join(output_dir, f"{lang}_obs_{version}_{story_padded}.frame_times.json")

    if not os.path.exists(transcription_path):
        transcribe_file(mp3_path, transcription_path, lang)

    flatten_transcription(transcription_path, flattened_path)
    tokenize_story_frames(md_path, story_data_path)
    fuzzy_merge_objects(story_data_path, flattened_path, merged_list_path)
    frame_times = get_frame_times(story_data_path, merged_list_path, frame_times_path)

    if frame_padded in frame_times:
        clip_path = mp3_path.replace("_128kbps.mp3", f"-{frame_padded}_128kbps.mp3")
        cut_mp3(mp3_path, frame_times[frame_padded]["start"], frame_times[frame_padded]["end"], clip_path)
        print(f"Clip is made. File: {clip_path}")
    else:
        print("Frame given is not found in the given story")
        exit(1)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Process an OBS story to produce an mp3 file for the given story's frame.")

    # Add the arguments
    parser.add_argument('--lang', type=str, default='en',
                    help='the language code (default: en)')
    parser.add_argument('--version', type=str, default='v6',
                    help='the OBS version (default: v6)')
    parser.add_argument('--story', type=int, default=1,
                    help='the OBS story number between 1 and 50 (default: 1)')
    parser.add_argument('--frame', type=int, default=1,
                    help='the frame number that a MP3 will be created for (default: 1)')
    parser.add_argument('--output', type=str, default="./output",
                    help='working directory for the output')

    # Parse the arguments
    args = parser.parse_args()
    
    process_story(args.lang, args.version, args.story, args.frame, args.output)
