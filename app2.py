from langchain_groq import ChatGroq
import streamlit as st
from langchain_core.messages import SystemMessage,AIMessage,HumanMessage

model = ChatGroq(model='llama-3.1-70b-versatile', api_key="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")
messages=[]
while True:
        query=str(input('what is your Prompt ?'))
        messages.append(HumanMessage(query))
        result=model.invoke(messages)
        print(result.content)
        messages.append(AIMessage(result.content))
