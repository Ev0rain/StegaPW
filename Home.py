import streamlit as st
from Main import add_password, retrieve_password, generate_key

st.set_page_config("Hello", page_icon="👋")

st.write("# Welcome to StegaPW! 👋")
st.markdown(
    """
    StegaPW is your **secure password management solution** using steganography!  
    With StegaPW, you can **encrypt passwords** and hide them seamlessly within images.  
    This ensures an additional layer of security through the combined power of:
    - **Encryption**: AES-based symmetric encryption ensures that your passwords remain safe.
    - **Steganography**: Embedding encrypted passwords within images keeps them hidden.

    ### How to Get Started:
    1. Navigate to **Generate Key 🔑** to create your encryption key.
    2. Generate images if you don't have any with the built in **Image Generator**.
    2. Use **Encode Password 🔒** to securely hide passwords in images.
    3. Retrieve your passwords anytime using **Decode Password 🔓**.

    ### Why Choose StegaPW?
    - Simple, secure, and user-friendly.
    - Combines modern cryptography and steganography techniques.
    - Designed with cybersecurity best practices in mind.

    Curious about the project? Check out the [GitHub repository](https://github.com/Ev0rain/StegaPW) for more details.
    """
)
