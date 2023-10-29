import gradio as gr
import os
import openai


openai.api_key = os.getenv("OPENAI_API_KEY") 

#inorder to list the available models to use further 
openai.Model.list()
openai.Model.retrieve("text-davinci-003")

#basic knowledge on using Chat Completion API
completion = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "Hello!"}
  ]
)

print(completion.choices[0].message)
print(completion)

#######################################################################################


# message_history = [{"role": "user", "content": f"You are a ghost bot. I will specify the subject matter in my messages, and you will reply with a dark joke that includes the subjects I mention in my messages. Reply only with jokes to further input in ghory manner. If you understand, say OK."},
#                    {"role": "assistant", "content": f"OK"}]
# def predict(input):
#     # tokenize the new input sentence
#     message_history.append({"role": "user", "content": f"{input}"})

#     completion = openai.ChatCompletion.create(
#       model="gpt-3.5-turbo",
#       messages=message_history
#     )
#     #Just the reply text
#     reply_content = completion.choices[0].message.content
    
#     message_history.append({"role": "assistant", "content": f"{reply_content}"}) 

#     response = [(message_history[i]["content"], message_history[i+1]["content"]) for i in range(2, len(message_history)-1, 2)]
#     return response


# with gr.Blocks() as demo: 

#     # creates a new Chatbot instance and assigns it to the variable chatbot.
#     chatbot = gr.Chatbot() 

#     # creates a new Row component, which is a container for other components.
#     with gr.Row(): 
#         txt = gr.Textbox(show_label=False, placeholder="Enter text and press enter").style(container=False)

#     txt.submit(predict, txt, chatbot) # submit(function, input, output)
#     #txt.submit(lambda :"", None, txt)  #Sets submit action to lambda function that returns empty string 

#     txt.submit(None, None, txt, _js="() => {''}") 
         
# demo.launch()