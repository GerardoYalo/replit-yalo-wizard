import streamlit as st

st.title("🚀 Mi app en Replit")
st.write("Editá este archivo y publicalo con un push.")

nombre = st.text_input("¿Cómo te llamás?")
if nombre:
    st.success(f"Hola, {nombre}! Tu app está viva 🎉")
