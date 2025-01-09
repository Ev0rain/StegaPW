import streamlit as st
from Main import add_password

st.set_page_config(page_title="Encode Password")

st.write("# Hide your password within an image")

# Encode password in image
st.header("Encode Password")
image_file = st.file_uploader("Upload Image", type=["png", "jpg"])
password = st.text_input("Password to Encode")
output_path = st.text_input("Output Image Path", "output_image.png")

if st.button("Encode"):
    if image_file and password and output_path:
        with open("temp_image.png", "wb") as f:
            f.write(image_file.read())
        add_password("temp_image.png", password, output_path)
        st.success(f"Password encoded and saved to {output_path}")
