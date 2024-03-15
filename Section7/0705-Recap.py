"""
Streamlit 을 이용한 챗봇 만들기 시작.

5. Recat : ChatMessage : chatGPT 와 같은 메시지 인터페이스를 만든다.
st.session_state : recap

and add import setting.
packageIndexDepths 의 값을 지정해서 잘 해줘야 쉽게 가져오는 것 같다.
langchain 작업중이니까 

#    python import 설정해서 해달라고 한건데... 안해도 되겠지?
    "pythonAutoImport.pythonInterpreterPath": "/Users/P170355/Downloads/study/fullstackGPT/env/bin/python",
    "python.analysis.packageIndexDepths": [
        {
            "name": "langchain",
            "depth": 5
        }
    ] /* 요렇게.. */



https://docs.streamlit.io
"""

from langchain.storage import LocalFileStore
import streamlit as st


st.title("test")

LocalFileStore()