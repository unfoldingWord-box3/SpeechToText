from faster_whisper import WhisperModel
// install using `pip install faster-whisper`

model_size = "large-v3"

# Run on GPU with FP16
# model = WhisperModel(model_size, device="cuda", compute_type="float16")

# or run on GPU with INT8
# model = WhisperModel(model_size, device="cuda", compute_type="int8_float16")
# or run on CPU with INT8
# model = WhisperModel(model_size, device="cpu", compute_type="int8")

model = WhisperModel(model_size, device="cpu", compute_type="int8")

sourceAudioFile = "./speech/obs/en/en_obs_02-05_128kbps.mp3"
segments, info = model.transcribe(sourceAudioFile, beam_size=5)

print("Detected language '%s' with probability %f" % (info.language, info.language_probability))

for segment in segments:
    print("[%.2fs -> %.2fs] %s" % (segment.start, segment.end, segment.text))