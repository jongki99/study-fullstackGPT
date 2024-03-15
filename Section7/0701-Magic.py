"""
Streamlit 을 이용한 챗봇 만들기 시작.

1. Magic ???

https://docs.streamlit.io/library/api-reference
"""

import streamlit as st
from langchain.chat_models import ChatOpenAI

st.selectbox("", ("", "GPT-3", "GPT-4",))

"""
    import 전과 후가 다르다.
    ### markdown 과는 다르겠지?
    #### 다른가?
    ##### 같은가?
    ###### 왜 같지?????
    ####### 이러면 정말 매직인가??
"""


"Magic.. 이렇게 하면 바로 출력되나??"
"되는데??"

a = [1,2,3,4]
b = {"x": 1, "y":2}

a
b

"여기부터는 write 단순 텍스트 출력은 편할지도???"

st.write("hello")

st.write(a)

st.write({"x":1})

st.write(ChatOpenAI) 
