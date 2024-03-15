"""
Streamlit 을 이용한 챗봇 만들기 시작.

3. Multi page

https://docs.streamlit.io
"""

import streamlit as st

st.set_page_config(
    page_title="FullstackGPT Home",
    page_icon="🤖",
)

st.title("Sidebar Home")

with st.sidebar:
    st.title("Side bar title")

    ti = st.text_input("text input", "")
    ti

tab_1, tab_2, tab_3 = st.tabs(["A", "B", "C"])
with tab_1:
    "aaa"
with tab_2:
    "bbb"
with tab_3:
    "ccc"

    st.markdown(
        """
    # Hello!
                
    Welcome to my FullstackGPT Portfolio!
                
    Here are the apps I made:
                
    - [ ] [DocumentGPT](/DocumentGPT)
    - [ ] [PrivateGPT](/PrivateGPT)
    - [ ] [QuizGPT](/QuizGPT)
    - [ ] [SiteGPT](/SiteGPT)
    - [ ] [MeetingGPT](/MeetingGPT)
    - [ ] [InvestorGPT](/InvestorGPT)
    """
    )