# Steganography Password Manager

## Project Description

This Python project is part of the coursework for the **BTS Cybersecurity** program at **Lycee Guillaume Kroll**. It demonstrates a steganographic approach to securely manage passwords by embedding and retrieving them from image files.
The project combines two important concepts:
- **Steganography**: Hiding information within images.
- **Encryption**: Protecting sensitive data using cryptographic techniques.

Users can securely store passwords by encrypting them and embedding the encrypted data within images. The project also supports retrieving and decrypting the hidden passwords.

## Features

- **Encryption and Decryption**: Uses AES-based symmetric encryption (via the `cryptography` library) to securely encode passwords.
- **Steganography**: Hides encrypted passwords within image files using the least significant bit (LSB) method.
- **Password Management**:
  - **Add Password**: Encrypts a password and embeds it into an image.
  - **Retrieve Password**: Extracts and decrypts a password hidden in an image.
- **Key Management**:
  - Generates and securely stores an encryption key for encrypting and decrypting passwords.

## Prerequisites and Installation

- Python 3.7+
- Clone the repository to your machine
- Install dependecies trough `requirements.txt`

```bash
pip install pillow cryptograph
```
## About
- Author:Liam Wolff
- Institution: Lycee Guillaume Kroll
- Course: BTS Cybersecurity
- Purpose: Python project demonstrating secure password management with steganography.
