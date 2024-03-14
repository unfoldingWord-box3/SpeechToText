# from faster_whisper import WhisperModel
import whisper_timestamped as whisper

model_size = "tiny"

model = whisper.load_model(name=model_size)

sourceAudioFile = "./speech/obs/en/en_obs_v6_01_128kbps.mp3"
# segments, info = model.transcribe(sourceAudioFile, beam_size=5)
results = whisper.transcribe(model, sourceAudioFile)

print("Detected language '%s' with probability %f" % (results["language"], results["language_probs"][results["language"]]))

for segment in results["segments"]:
    print("[%.2fs -> %.2fs] %s" % (segment["start"], segment["end"], segment["text"]))
