"""
Streamlit 을 이용한 챗봇 만들기 시작.

2. Streamlit Dataflow
    html component 의 내용을 바꾸면, 전체가 재실행된다.
    서버 사이드 아닌가????
    까다롭구만...

https://docs.streamlit.io
"""

import streamlit as st
from datetime import datetime

today = datetime.today().strftime("%H:%M:%S")

st.title(today)

model = st.selectbox(
    "Choose your model",
    (
        "GPT-3",
        "GPT-4",
    ),
)

if model == "GPT-3":
    st.write("cheap")
else:
    st.write("not cheap")
    name = st.text_input("What is your name?")
    st.write(name)

    value = st.slider(
        "temperature",
        min_value=0.1,
        max_value=1.0,
    )

    st.write(value)
    