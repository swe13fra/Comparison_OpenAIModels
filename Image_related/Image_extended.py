import os
import openai
openai.api_key = os.getenv("OPENAI_API_KEY")
response = openai.Image.create_variation(
  image=open("original.png", "rb"),
  n=3,
  size="1024x1024"
)


image_url1 = response['data'][0]['url']
image_url2 = response['data'][1]['url']
image_url3 = response['data'][2]['url']
print(image_url1, image_url2,image_url3)