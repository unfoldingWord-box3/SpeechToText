from faster_whisper import WhisperModel

model_size = "large-v3"
# sourceAudioFile = "./speech/obs/en/en_obs_02-05_128kbps.mp3"
# sourceAudioFile = "speech/obs/fr/fr_obs_01_128kbps.mp3"
# sourceAudioFile = "speech/obs/ylb/ylb_obs_09_128kbps.mp3"
sourceAudioFile = "speech/obs/kn/kn_obs_09_64kbps.mp3"

# Run on GPU with FP16
# model = WhisperModel(model_size, device="cuda", compute_type="float16")

# or run on GPU with INT8
# model = WhisperModel(model_size, device="cuda", compute_type="int8_float16")
# or run on CPU with INT8
# model = WhisperModel(model_size, device="cpu", compute_type="int8")

print("Opening Model")
model = WhisperModel(model_size, device="auto", compute_type="int8")

print(f"Transcribing Audio for {sourceAudioFile}")
segments, info = model.transcribe(sourceAudioFile, beam_size=5)

print("Detected language '%s' with probability %f" % (info.language, info.language_probability))

for segment in segments:
    print("[%.2fs -> %.2fs] %s" % (segment.start, segment.end, segment.text))