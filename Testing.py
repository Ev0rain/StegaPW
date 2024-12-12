from Main import encode_data_in_image
from PIL import Image

img = Image.new("RGB", (100, 100), color="white")
img.save("test_image.png")

# Testing encode feature
encode_data_in_image("test_image.png", "Hello, World!", "encoded_image.png")
