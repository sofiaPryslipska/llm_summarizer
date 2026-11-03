import streamlit as st
from google import genai
from google.genai import types

st.title("Текстовий сумаризатор")

# Поля вводу
api_key = st.text_input("Введіть Gemini API Key", type="password")
text = st.text_area("Введіть текст для сумаризації", height=200)

# Кнопка запуску
if st.button("Сумаризувати"):
    if not api_key:
        st.error("Помилка: Введіть API key")
    elif not text:
        st.warning("Помилка: Введіть текст")
    else:
        try:
            client = genai.Client(api_key=api_key)
            response = client.models.generate_content(
                model='gemini-2.5-flash',
                contents=text,
                config=types.GenerateContentConfig(
                    system_instruction='summarize this text without any greetings and introduction.only the result!'
                )
            )
            # Виведення результату
            st.success("Результат:")
            st.write(response.text)
        except Exception as e:
            st.error(f"Виникла помилка: {str(e)}")