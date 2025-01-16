import streamlit as st
from Main import retrieve_password
import os

st.set_page_config(page_title="Decode Password,", page_icon="🔓")

st.write("# Retrieve your password from an Image 🔓")

st.markdown(
    """
    ### Retrieve Hidden Passwords
    This tool extracts and decrypts passwords hidden within image files.

    ### Steps:
    1. Upload the image file containing the hidden password.
    2. Click "Decode" to retrieve the password.

    **:red[Important]**: Ensure the encryption key (`secret.key`) is present, as it’s required for decryption.
    """
)

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
        finally:
            os.remove("temp_decode_image.png")
