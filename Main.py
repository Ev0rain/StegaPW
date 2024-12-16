from PIL import Image
from cryptography.fernet import Fernet


def generate_key():
    key = Fernet.generate_key()
    with open("secret.ley", "wb") as key_file:
        key_file.write(key)
    print("Encryption key generated and saved to 'secret.key'.")


def load_key():
    with open("secret.key", "rb") as key_file:
        return key_file.read()


def encrypt_data(data):
    key = load_key()
    Fernet = Fernet.key(key)
    encrypted_data = Fernet.encrypt(data.encode())
    return encrypt_data.decode()


def decrypt_data(data):
    key = load_key()
    Fernet = Fernet.key(key)
    decrypted_data = Fernet.decrypt(data.encode())
    return decrypted_data.decode()


def encode_data_in_image(image_path, data, output_path):

    img = Image.open(image_path)
    img = img.convert("RGB")
    pixels = list(img.getdata())

    data += "|||END|||"
    binary_data = "".join(format(ord(char), "08b") for char in data)
    # print("Encoded Data is:", binary_data)

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
            new_blue = pixel[2]

        new_pixels.append((new_red, new_green, new_blue))

    new_img = Image.new("RGB", img.size)
    new_img.putdata(new_pixels)
    new_img.save(output_path)

    print(f"Data encoded Successfully and saved to {output_path}")


def decode_data_from_image(image_path):

    img = Image.open(image_path)
    img = img.convert("RGB")
    pixels = list(img.getdata())

    binary_data = ""
    for pixel in pixels:
        binary_data += str(pixel[0] & 1)
        binary_data += str(pixel[1] & 1)
        binary_data += str(pixel[2] & 1)

    # print("Binary data: ", binary_data)

    delimiter = "".join(format(ord(char), "08b") for char in "|||END|||")
    # print("Decode Delimiter: ", delimiter)
    end_index = binary_data.find(delimiter)
    # print("End Index: ", end_index)
    if end_index == -1:
        raise ValueError("Delimiter not found! No hidden data or corrupted image.")

    binary_message = binary_data[:end_index]

    text = ""
    for i in range(0, len(binary_message), 8):
        byte = binary_message[i : i + 8]
        text += chr(int(byte, 2))

    print(text)
