import streamlit as st
from Main import add_password
import os

st.set_page_config(page_title="Encode Password", page_icon="🔒")

st.write("# Hide your password within an image 🔒")

st.markdown(
    """
    ### Hide Your Passwords Securely
    This tool allows you to embed an encrypted password within an image file.

    ### Steps:
    1. Upload an image file (PNG or JPG recommended).
    2. Enter the password you want to hide.
    3. Specify a name for the output image file.
    4. Click "Encode" to hide your password.
    
    **:red[Important]**: Ensure the encryption key (`secret.key`) is present, as it’s required for decryption.

    **Tip**: Choose a high-resolution image to accommodate more hidden data.
    """
)

# Encode password in image
st.header("Encode Password")
image_file = st.file_uploader("Upload Image", type=["png", "jpg"])
password = st.text_input("Password to Encode", type="password")
st.markdown(" - Make sure to use a strong password")
output_name = st.text_input("Output Image Name", "output_image.png")

if st.button("Encode"):
    if image_file and password and output_name:
        with open("temp_image.png", "wb") as f:
            f.write(image_file.read())
        try:
            add_password("temp_image.png", password, output_name)
            st.success(f"Password encoded and saved to {output_name}")
        finally:
            os.remove("temp_image.png")
