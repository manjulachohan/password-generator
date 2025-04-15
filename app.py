# Project: Pasword Genertor In Python
import streamlit as st
import random
import string

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choices(characters, k=length))
    return password
# Streamlit App
st.title("🔐 Password Generator")


length = st.number_input("Enter the length of your desired password:", min_value=4, max_value=100, value=12, step=1)

if st.button("Generate Password"):
   password = generate_password(length)
   st.success(f"You Generated password: `{password}`")
