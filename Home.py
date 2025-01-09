import streamlit as st
from Main import add_password, retrieve_password, generate_key

st.title("Steganography Password Manager")

# Generate encryption key
if st.button("Generate Encryption Key"):
    generate_key()
    st.success("Encryption key generated and saved.")

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

# Decode password from image
st.header("Decode Password")
decode_image_file = st.file_uploader("Upload Image to Decode", type=["png", "jpg"])

if st.button("Decode"):
    if decode_image_file:
        with open("temp_decode_image.png", "wb") as f:
            f.write(decode_image_file.read())
        try:
            password = retrieve_password("temp_decode_image.png")
            st.success(f"Retrieved Password: {password}")
        except Exception as e:
            st.error(f"Error: {e}")
