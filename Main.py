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
        if binary_index < len(binary_data):
            new_red = (pixel[0] & ~1) | int(binary_data[binary_index])
            binary_index += 1
        else:
            new_red = pixel[0]

        if binary_index < len(binary_data):
            new_green = (pixel[1] & ~1) | int(binary_data[binary_index])
            binary_index += 1
        else:
            new_green = pixel[1]

        if binary_index < len(binary_data):
            new_blue = (pixel[2] & ~1) | int(binary_data[binary_index])
            binary_index += 1
        else:
            new_green = pixel[2]

        new_pixels.append((new_red, new_green, new_blue))

    new_img = Image.new("RGB", img.size)
    new_img.putdata(new_pixels)
    new_img.save(output_path)
