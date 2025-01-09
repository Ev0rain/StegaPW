import streamlit as st
from Main import generate_key

st.set_page_config(page_title="Generate Key", page_icon="🔑")

st.write("# Generate your key 🔑")

st.markdown(
    """
    To encrypt and decrypt your passwords, you need a key.  
    This will generate a key for you, that will be used for encryption and decryption.
    """
)

# Generate encryption key
if st.button("Generate Encryption Key"):
    generate_key()
    st.success("Encryption key generated and saved.")
