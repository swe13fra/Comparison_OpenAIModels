import os
import openai
import json

openai.api_key = os.getenv("OPENAI_API_KEY")
GPT_MODEL = "gpt-3.5-turbo-0613"

def get_fruit_color(fruit):
    fruit_details = {
        "fruit" : fruit
    }
    return json.dumps(fruit_details)
def runthefun():
    functions = [
    {
        "name": "get_fruit_color",
        "description": "Get the color of the fruit",
        "parameters":{
            "type": "object",
            "properties": {
                "fruit":{
                    "type": "string",
                    "description": "Name of the fruit, e.g. Apple, Banana, Coconut"
                }
            },
            "required": ["fruit"],
        },
    }
  ]

    prompt  = "What is the color of Custard apple."

    messages = []
    messages.append({"role": "user", "content": prompt})

    response = openai.ChatCompletion.create(model = GPT_MODEL,
                                        messages = messages,
                                        functions = functions,
                                        function_call ="auto",
    )

    #if function_call is auto
    message = response["choices"][0]["message"]
    if message.get("function_call"):
        function_name = message["function_call"]["name"]

    else:
        if response["choices"][0]["finish_reason"] == "function_call":
            print("Call a function")

    response = get_fruit_color(
        fruit = eval(message["function_call"]["arguments"]).get("fruit"))

    final_response = openai.ChatCompletion.create(
        model = GPT_MODEL,
        messages = [
            {"role":"user", "content":prompt},
            message,
            {
                "role": "function",
                "name": function_name,
                "content": response,
            }
        ]
    )
 
    return final_response['choices'][0]['message']['content']


print(runthefun())