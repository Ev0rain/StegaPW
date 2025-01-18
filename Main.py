from PIL import Image, ImageDraw
from cryptography.fernet import Fernet
import base64
import os


# Generate a new encryption key
def generate_key():

    # Create a directory for keys if it doesn't exist
    if not os.path.exists("keys"):
        os.makedirs("keys")

    # Define the path to save the encryption key
    key_file_path = os.path.join("keys", "secret.key")

    # Generate a secure symmetric encryption key
    key = Fernet.generate_key()
    with open(key_file_path, "wb") as key_file:
        key_file.write(key)

    print("Encryption key generated and saved to 'secret.key'.")


# Load encryption key from file
def load_key():

    # Define the path to the key file
    key_file_path = os.path.join("keys", "secret.key")

    # Check if the key file exists
    if not os.path.exists(key_file_path):
        raise FileNotFoundError(
            f"Key not found in '{key_file_path}'. Please generate or add your secret.key file"
        )

    # Read and return the key from the file
    with open(key_file_path, "rb") as key_file:
        return key_file.read()


# Encrypt data using the loaded key
def encrypt_data(data):

    # Load the encryption key
    key = load_key()
    f = Fernet(key)

    # Encrypt the input data and encode it in Base64 for compatibility
    encrypted_data = f.encrypt(data.encode())
    return base64.b64encode(encrypted_data).decode()


# Decrypt data using the loaded key
def decrypt_data(data):

    # Load the encryption key
    key = load_key()
    f = Fernet(key)

    # Decode the Base64 data and decrypt it
    encrypted_data = base64.b64decode(data.encode())
    decrypted_data = f.decrypt(encrypted_data)
    return decrypted_data.decode()


# Hide encrypted data witin an imange using LSB steganography
def encode_data_in_image(image_path, data, output_path):

    # Open the input image and ensure it is in RGB format
    img = Image.open(image_path)
    img = img.convert("RGB")
    pixels = list(img.getdata())

    data += "|||END|||"  # Append delimieter to indicate the end of hidden data
    binary_data = "".join(format(ord(char), "08b") for char in data)

    # Ensure the image has enough capacity to hide the data
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

        # Append the modified pixel to the new pixel list
        new_pixels.append((new_red, new_green, new_blue))  # Append modified pixel

    # Create a new image with the modified pixel data
    new_img = Image.new("RGB", img.size)
    new_img.putdata(new_pixels)
    new_img.save(output_path)

    print(f"Data encoded Successfully and saved to {output_path}")


# Retrieve encrypted data from an image using LSB steganography
def decode_data_from_image(image_path):

    # Open the input image and ensure it is in RGB format
    img = Image.open(image_path)
    img = img.convert("RGB")
    pixels = list(img.getdata())

    # Extract binary data from the LSBs of the pixels
    binary_data = ""
    for pixel in pixels:
        binary_data += str(pixel[0] & 1)  # Exctract LSB from red channel
        binary_data += str(pixel[1] & 1)  # Exctract LSB from green channel
        binary_data += str(pixel[2] & 1)  # Exctract LSB from blue channel

    # Define the binary delimiter indicating the end of the hidden data
    delimiter = "".join(format(ord(char), "08b") for char in "|||END|||")
    end_index = binary_data.find(delimiter)  # Find the delimiter in the binary data
    if end_index == -1:
        raise ValueError("Delimiter not found! No hidden data or corrupted image.")

    # Extract the binary message up to the delimiter
    binary_message = binary_data[:end_index]  # Extract data before the delimiter

    # Convert the binary message into characters
    decoded_data = ""
    for i in range(0, len(binary_message), 8):
        byte = binary_message[i : i + 8]
        decoded_data += chr(int(byte, 2))
    return decoded_data


# Encrypt and embedd a password in an image
def add_password(image_path, password, output_path):
    # Encrypt the password
    encrypted_password = encrypt_data(password)

    # Embed the encrypted password in the image
    encode_data_in_image(image_path, encrypted_password, output_path)


# Retrieve and decrypt a password from an image
def retrieve_password(image_path):
    # Extract the encrypted password from the image
    encrypted_password = decode_data_from_image(image_path)
    # Decrypt and return the original password
    return decrypt_data(encrypted_password)


# Generate an image with optional patterns (e.g., grid or stripes)
def generate_image(
    width, height, color, pattern=None, output_path="generated_image.png"
):
    # Create a new image with the specified dimensions and background color
    img = Image.new("RGB", (width, height), color)
    draw = ImageDraw.Draw(img)

    # Apply a grid pattern if selected
    if pattern == "grid":
        for x in range(0, width, 10):
            draw.line((x, 0, x, height), fill=(255, 255, 255), width=1)
        for y in range(0, height, 10):
            draw.line((0, y, width, y), fill=(255, 255, 255), width=1)
    # Apply a stripes pattern if selected
    elif pattern == "stripes":
        for y in range(0, height, 10):
            draw.rectangle((0, y, width, y + 5), fill=(255, 255, 255))

    # Save the generated image to the specified output path
    img.save(output_path)
    return output_path
