from base64 import b64decode
import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")


response = openai.Image.create_edit(
  image=open("original.png", "rb"),
  mask=open("mask.png", "rb"),
  prompt="A golden retriever wearing a yellow cape and a beret",
  n=3,
  size="1024x1024"
)

image_url1 = response['data'][0]['url']
image_url2 = response['data'][1]['url']

print(image_url1, image_url2)