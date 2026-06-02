import streamlit as st

with open("system_prompt.txt", "r") as f:
    system_prompt = f.read()

st.title("System Prompt Bot")

question = st.text_input("Ask")

if st.button("Submit"):
    st.write("System Prompt:")
    st.write(system_prompt)
    st.write("Question:")
    st.write(question)
