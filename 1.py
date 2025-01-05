import argparse
from encryptor.aes_encryption import encrypt_file, decrypt_file
from encryptor.file_handler import validate_file, get_output_path

def main():
    parser = argparse.ArgumentParser(description="AES-256 File Encryption Tool")
    parser.add_argument("action", choices=["encrypt", "decrypt"], help="Action to perform")
    parser.add_argument("file", help="Path to the input file")
    parser.add_argument("password", help="Password for encryption/decryption")
    args = parser.parse_args()
    if not validate_file(args.file):
        print(f"Error: File '{args.file}' does not exist.")
        return
    if args.action == "encrypt":
        output_path = get_output_path(args.file, "encrypted")
        encrypt_file(args.file, args.password, output_path)
        print(f"File encrypted successfully: {output_path}")
    elif args.action == "decrypt":
        output_path = get_output_path(args.file, "decrypted")
        decrypt_file(args.file, args.password, output_path)
        print(f"File decrypted successfully: {output_path}")

if __name__ == "__main__":
    main()
