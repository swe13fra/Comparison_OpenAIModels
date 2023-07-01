import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

audio_file = open("german_song.mp4", "rb")
translate = openai.Audio.translate("whisper-1", audio_file)


print(translate["text"])
#or write the converted text into a text document
with open("translated.txt", "w") as f:
    f.write(translate["text"])