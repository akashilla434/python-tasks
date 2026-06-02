import streamlit as st

st.title("Gemini Streamlit Bot")

question = st.text_input("Ask a Question")

if st.button("Ask"):
    st.write("You asked:", question)
