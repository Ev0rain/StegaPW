import Main
import os
from PIL import Image

if os.path.exists("encoded_image.png"):
    os.remove("encoded_image.png")
if os.path.exists("test_image.png"):
    os.remove("test_image.png")

img = Image.new("RGB", (100, 100), color="white")
img.save("test_image.png")

# Testing encode feature
Main.encode_data_in_image("test_image.png", "Hello, World!", "encoded_image.png")

Main.decode_data_from_image("encoded_image.png")
