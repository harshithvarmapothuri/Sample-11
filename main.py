from langchain.llms import OpenAI
import streamlit as st
from constants import openai_key
import os
os.environ["OPENAI_API_KEY"]=openai_key
st.title("My App")
inp=st.text_input("Enter a celbrit name to find birthday")

llm=OpenAI(temperature=0.7,verbose=True)

kk='Find the birthday of '+inp
if inp:
    st.write(llm(kk))