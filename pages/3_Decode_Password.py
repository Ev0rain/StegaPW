import streamlit as st
from Main import retrieve_password

st.set_page_config(page_title="Decode Password")

st.write("# Retrieve your password from an Image")

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
