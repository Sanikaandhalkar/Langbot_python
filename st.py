import streamlit as st
import openai        
import speech_recognition as sr     

# list of messeges where we will append all questions asked by user and also responses given by chatgpt
messages =[]
# creating fuction so we can ask answers from chat gpt for questions given bt user

def ast_question(question):
    messages.append({'role':'user','content':'question'})              #Add questions in dictionary format 
    # generate response
    response = openai.chat.completions.create(
        model = 'gpt-3.5-turbo' ,
        meseges = messages 
    )
    print(response)

    # we will use best choice given in response by chatgpt
    ChatGPT_reply = response.choices[0].message.content
    print(ChatGPT_reply)
    messages.append({'role':'asistant','content':'ChatGPT_reply'})


    return ChatGPT_reply
()
st.write(ast_question('Hello'))
