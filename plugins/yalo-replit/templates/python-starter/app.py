import streamlit as st

st.title("🚀 My app on Replit")
st.write("Edit this file and publish it with a push.")

name = st.text_input("What's your name?")
if name:
    st.success(f"Hey, {name}! Your app is live 🎉")
