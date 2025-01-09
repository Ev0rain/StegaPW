import streamlit as st
from Main import generate_key

st.set_page_config(page_title="Generate Key")

st.write("# Generate your key")

# Generate encryption key
if st.button("Generate Encryption Key"):
    generate_key()
    st.success("Encryption key generated and saved.")
