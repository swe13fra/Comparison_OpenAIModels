from base64 import b64decode
import os
import openai


openai.api_key = "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"
#openai.Model.list()

# Option 1
# using image creation api with url as result
response = openai.Image.create(
    prompt = "dancing bear in space",
    n = 2,
    size = "512x512"
)

# need to change this into more general form
image_url1 = response['data'][0]['url']
image_url2 = response['data'][1]['url']

print(image_url1, image_url2)

# Option 2
# using image creation api with json as result
def generateImimage_urlage(prompt, image_count):
    images = []
    response = openai.Image.create(
        prompt = prompt,
        n = image_count,
        size = '1024x1024',
        response_format ='b64_json'
    )

    for image in response['data']:
        images.append(image.b64_json)

    prefix = 'Pic'
    for index,image in enumerate(images):
        with open(f'{prefix}_{index}.jpg', 'wb')as file:
            file.write(b64decode(image))

openai.api_key = os.getenv("OPENAI_API_KEY") #Have added the OpenAI API key to the environment variable and use it here directly

generateImimage_urlage('Golden retriever wearing a cape realistic image', image_count=3)