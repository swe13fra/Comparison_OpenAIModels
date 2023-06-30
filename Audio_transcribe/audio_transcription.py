import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

audio_file = open("audio_file.mp4", "rb")
transcript = openai.Audio.transcribe("whisper-1", audio_file)


print(transcript["text"])
#or write the converted text into a text document
with open("transcribed.txt", "w") as f:
    f.write(transcript["text"])