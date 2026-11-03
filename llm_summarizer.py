import streamlit as st
from google import genai
from google.genai import types

st.title("Text summarizer")
st.write("This tool generates a quick and concise summary of any provided text using the Gemini 2.5 Flash model.")

api_key = st.text_input("Enter your API Key", type="password")
text = st.text_area("Enter the text", height=200)

if st.button("Summarize"):
    if not api_key:
        st.error("Error: Please enter your API key")
    elif not text:
        st.warning("Error: Please enter the text")
    else:
        try:
            client = genai.Client(api_key=api_key)
            response = client.models.generate_content(
                model='gemini-2.5-flash',
                contents=text,
                config=types.GenerateContentConfig(
                    system_instruction='Vey briefly summarize this text without any greetings and introduction. Only output the result.'
                )
            )
            
            st.success("Result:")
            st.write(response.text)
        except Exception as e:
            st.error(f"An error occurred: {str(e)}")
