# app.py

import streamlit as st

st.title("안녕하세요, Streamlit 앱 테스트")
st.write("이것은 Windows 환경에서 실행하는 예제입니다.")

# 간단한 입력 위젯 예시
name = st.text_input("이름을 입력하세요")
if name:
    st.write(f"반갑습니다, {name}님!")

