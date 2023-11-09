import openai
import streamlit as st
st.text('Code Explanation AI')

openai.api_key="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"

#method to print and update the message list with repsonse from gpt model.

def get_gpt_response(messages):
    response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=messages
)
    print(response['choices'][0]['message']['content'])
    return response['choices'][0]['message']['content']
#method to update the message list with user prompt.

def update_chat(messages,role,content):
    messages.append({'role':role,'content':content})
    return messages

messages=[
        {"role": "system", "content": "You are a trained to stepwise explain the code snippets."}
         ]
print(messages[0]['content'])
while True:
    user_input=input()
    messages=update_chat(messages,'user',user_input)
    model_response=get_gpt_response(messages)
    messages=update_chat(messages,'assistant',model_response)

