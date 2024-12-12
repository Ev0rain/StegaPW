from PIL import Image


def encode_data_in_image(image_path, data, output_path):

    img = Image.open(image_path)
    img = img.convert("RGB")
    pixels = list(img.getdata())

    data += "|||END|||"
    binary_data = "".join(format(ord(char), "08b") for char in data)

    if len(binary_data) > len(pixels) * 3:
        raise ValueError("Image is too small to hide thise data!")

    new_pixels = []
    binary_index = 0
    for pixel in pixels:
        if binary_index > len(binary_data):
            new_red = (pixel[0] & ~1) | int(binary_data[binary_index])
            binary_index += 1
