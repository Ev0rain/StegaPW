import streamlit as st
from Main import generate_image

st.set_page_config(page_title="Image Generator", page_icon="🎨")

st.write("# Generate Images for StegaPW 🎨")

# Generate Image
width = st.number_input("Width (px)", value=300, min_value=10, step=10)
height = st.number_input("Height (px)", value=300, min_value=10, step=10)
color = st.color_picker("Background Color", value="#0000FF")
pattern = st.selectbox("Select Pattern", options=[None, "grid", "stripes"])
output_path = st.text_input("Output Image Path", "generated_image.png")

if st.button("Generate Image"):
    rgb_color = tuple(int(color[i : i + 2], 16) for i in (1, 3, 5))
    image_path = generate_image(width, height, rgb_color, pattern, output_path)
    st.image(image_path, caption="Generated Image")
    st.success(f"Image saved to {output_path}")
