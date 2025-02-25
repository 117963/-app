import streamlit as st

st.title("我的第一个应用 🚀")
st.write("恭喜！手机上传成功！")
name = st.text_input("输入你的名字：")
if name:
    st.write(f"你好，{name}！")
