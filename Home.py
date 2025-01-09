import streamlit as st
from Main import add_password, retrieve_password, generate_key

st.set_page_config("Hello", page_icon="👋")

st.write("# Welcome to StegaPW! 👋")
st.markdown(
    """
    StegaPW is a steganographic password manager, using images to hide your passwords.
    ### Want to learn more?
    - Check out my [github](https://github.com/Ev0rain/StegaPW)
    """
)
