import streamlit as st
import importlib

st.set_page_config( page_title="设计模式演示",layout="wide",initial_sidebar_state="expanded)

title = st.sidebar.radio("语言/Language", ["中文", "Русский"])
if title == "Русский":
    st.title("Добро пожаловать")
else:
    st.title("欢迎")

if title == "Русский":
    selected = st.sidebar.selectbox("Выберите презентацию")
else:
    selected = st.sidebar.selectbox("选择设计模式")







