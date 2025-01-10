from PIL import Image, ImageDraw
from cryptography.fernet import Fernet
import base64


# Generate a new encryption key
def generate_key():
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)
    print("Encryption key generated and saved to 'secret.key'.")


# Load encryption key from file
def load_key():
    with open("secret.key", "rb") as key_file:
        return key_file.read()


# Encrypt data using the loaded key
def encrypt_data(data):
    key = load_key()
    f = Fernet(key)
    encrypted_data = f.encrypt(data.encode())
    return base64.b64encode(encrypted_data).decode()


# Decrypt data using the loaded key
def decrypt_data(data):
    key = load_key()
    f = Fernet(key)
    encrypted_data = base64.b64decode(data.encode())
    decrypted_data = f.decrypt(encrypted_data)
    return decrypted_data.decode()


# Hide encrypted data witin an imange using LSB steganography
def encode_data_in_image(image_path, data, output_path):

    img = Image.open(image_path)
    img = img.convert("RGB")
    pixels = list(img.getdata())

    data += "|||END|||"  # Append delimieter to indicate the end of hidden data
    binary_data = "".join(format(ord(char), "08b") for char in data)

    if len(binary_data) > len(pixels) * 3:  # Ensure data has enough capacity
        raise ValueError("Image is too small to hide this data!")

    # Modify the LSBs of the pixels
    new_pixels = []
    binary_index = 0
    for pixel in pixels:
        if binary_index < len(binary_data):  # Modify the red channel
            new_red = (pixel[0] & ~1) | int(binary_data[binary_index])
            binary_index += 1
        else:
            new_red = pixel[0]

        if binary_index < len(binary_data):  # Modify the green channel
            new_green = (pixel[1] & ~1) | int(binary_data[binary_index])
            binary_index += 1
        else:
            new_green = pixel[1]

        if binary_index < len(binary_data):  # Modify the blue channel
            new_blue = (pixel[2] & ~1) | int(binary_data[binary_index])
            binary_index += 1
        else:
            new_blue = pixel[2]

        new_pixels.append((new_red, new_green, new_blue))  # Append modified pixel

    new_img = Image.new("RGB", img.size)
    new_img.putdata(new_pixels)
    new_img.save(output_path)

    print(f"Data encoded Successfully and saved to {output_path}")


# Retrieve encrypted data from an image using LSB steganography
def decode_data_from_image(image_path):

    img = Image.open(image_path)
    img = img.convert("RGB")
    pixels = list(img.getdata())

    binary_data = ""
    for pixel in pixels:
        binary_data += str(pixel[0] & 1)  # Exctract LSB from red channel
        binary_data += str(pixel[1] & 1)  # Exctract LSB from green channel
        binary_data += str(pixel[2] & 1)  # Exctract LSB from blue channel

    delimiter = "".join(format(ord(char), "08b") for char in "|||END|||")
    end_index = binary_data.find(delimiter)  # Find the delimiter in the binary data
    if end_index == -1:
        raise ValueError("Delimiter not found! No hidden data or corrupted image.")

    binary_message = binary_data[:end_index]  # Extract data before the delimiter

    decoded_data = ""
    for i in range(0, len(binary_message), 8):
        byte = binary_message[i : i + 8]
        decoded_data += chr(int(byte, 2))
    return decoded_data


# Encrypt and embedd a password in an image
def add_password(image_path, password, output_path):
    encrypted_password = encrypt_data(password)
    encode_data_in_image(image_path, encrypted_password, output_path)


# Retrieve and decrypt a password from an image
def retrieve_password(image_path):
    encrypted_password = decode_data_from_image(image_path)
    return decrypt_data(encrypted_password)


def generate_image(
    width, height, color, pattern=None, output_path="generated_iamge.png"
):
    img = Image.new("RGB", (width, height), color)
    draw = ImageDraw.Draw(img)

    if pattern == "grid":
        for x in range(0, width, 10):
            draw.line((x, 0, x, height), fill=(255, 255, 255), width=1)
        for y in range(0, height, 10):
            draw.line((0, y, width, y), fill=(255, 255, 255), width=1)
    elif pattern == "stripes":
        for y in range(0, height, 10):
            draw.rectangle((0, y, width, y + 5), fill=(255, 255, 255))

    img.save(output_path)
    return output_path
