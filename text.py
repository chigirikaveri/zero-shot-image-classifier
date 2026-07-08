import whisper
model = whisper.load_model("base")
result=model.transcribe("speech.mp3")
print(result["text"])
