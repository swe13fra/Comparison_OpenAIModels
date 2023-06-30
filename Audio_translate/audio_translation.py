import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

audio_file = open("german_song.mp4", "rb")
transcript = openai.Audio.transcribe("whisper-1", audio_file)
#translate = openai.Audio.translate("whisper-1", audio_file)


print(transcript["text"])#,translate["text"])
#or write the converted text into a text document
# with open("translated.txt", "w") as f:
#     f.write(translate["text"])