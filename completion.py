import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

response = openai.Completion.create(
  model="gpt-3.5-turbo-instruct",
  prompt="Give me the code for fibonnaci series of n numbers.",
  max_tokens=200,
  temperature=0
)

print(response.choices[0])