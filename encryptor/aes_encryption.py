import os
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC 
from cryptography.hazmat.primitives import hashes 
from cryptography.hazmat.backends import default_backend 
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes 

def generate_key(password: str, salt: bytes) -> bytes:
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )
    return kdf.derive(password.encode())

def encrypt_file(input_path: str, password: str, output_path: str) -> None:
    salt = os.urandom(16)
    iv = os.urandom(16)
    key = generate_key(password, salt)
    cipher = Cipher(algorithms.AES(key), modes.CFB(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    with open(input_path, 'rb') as infile:
        plaintext = infile.read()
    ciphertext = encryptor.update(plaintext) + encryptor.finalize()
    with open(output_path, 'wb') as outfile:
        outfile.write(salt + iv + ciphertext)

def decrypt_file(input_path: str, password: str, output_path: str) -> None:
    with open(input_path, 'rb') as infile:
        data = infile.read()
    salt, iv, ciphertext = data[:16], data[16:32], data[32:]
    key = generate_key(password, salt)
    cipher = Cipher(algorithms.AES(key), modes.CFB(iv), backend=default_backend())
    decryptor = cipher.decryptor()
    plaintext = decryptor.update(ciphertext) + decryptor.finalize()
    with open(output_path, 'wb') as outfile:
        outfile.write(plaintext)
