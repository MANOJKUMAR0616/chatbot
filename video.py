import google.generativeai as genai

genai.configure(api_key='AIzaSyAqPncS1ME92ebiWLrtoWZgH_we66RRy7Y')

model = genai.GenerativeModel('gemini-pro')

chat = model.start_chat(history=[])

import streamlit as st 
import os

def chat_bot(questions):
    response =chat.send_message(questions,stream = True)
    return response

st.set_page_config(page_title = 'Q&A demo')
st.header('LLM chatbot')
inputt = st.text_input("input:",key = "input")
submit = st.button("Ask the question")

if inputt and submit:
    response = chat_bot(inputt)
    st.subheader("the response is")
    for chunk in response:
        st.write(chunk.text)