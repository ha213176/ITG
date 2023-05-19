import whisper

# tiny < base < small < medium < large
model = whisper.load_model("small")
result = model.transcribe("./example3.mp3")
print(result["text"])