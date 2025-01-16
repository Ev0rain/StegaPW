import streamlit as st
from Main import generate_key

st.set_page_config(page_title="Generate Key", page_icon="🔑")

st.write("# Generate your key 🔑")

st.markdown(
    """
    ### What is a Key?
    The encryption key is a **unique secret** that encrypts and decrypts your passwords.  
    Without it, you won't be able to retrieve your stored passwords.

    ### Instructions:
    1. Click the button below to generate a secure key.
    2. The key will be saved locally as a file named `secret.key`.
    3. Ensure you keep this file safe, as it’s crucial for decrypting your passwords.

    **Note**: Losing the key means losing access to your passwords!
    """
)

# Generate encryption key
if st.button("Generate Encryption Key"):
    generate_key()
    st.success("Encryption key generated and saved.")
