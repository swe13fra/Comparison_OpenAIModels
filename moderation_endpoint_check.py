import os
import openai
openai.api_key = os.getenv("OPENAI_API_KEY")
response = openai.Moderation.create(
  input="I want to commit suicide",
)

print(response)
