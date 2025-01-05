Name: PRANJALI VITTHAL CHAVAN

Company: CODTECH IT SOLUTIONS

Intern ID: CT08DHG

Domain: Cyber Security & Ethical Hacking

Duration: December 2024 to January 2025

Mentor: Neela Santhosh Kumar

Overview of the Project

Project: Create tool for ADVANCED ENCRYPTION TOOL

Objective:-
The Advanced Encryption Tool uses AES-256 encryption to ensure the confidentiality and security of files. It allows users to encrypt or decrypt files with a password, protecting sensitive data from unauthorized access during storage or sharing. By incorporating a strong encryption method, random salt, and IV generation, the tool ensures enhanced security for every file. It validates input files before processing and creates new output files to prevent accidental overwriting. Designed for simplicity, it features a command-line interface for quick and efficient use. The tool safeguards sensitive data and makes it accessible only to users with the correct password, providing a reliable way to protect private information.

Key Activities:-
1. Key Generation: Uses PBKDF2HMAC with SHA-256 to derive a secure key from the user's password and a unique salt, ensuring strong encryption.

2. File Encryption: Encrypts files with AES-256 in CFB mode, generating a unique salt and IV for each process to enhance security.

3. File Decryption: Decrypts files by extracting the salt, IV, and ciphertext, then regenerating the key using the password and salt.

4. Salt and IV Handling: Combines salt, IV, and ciphertext into the output file for seamless decryption later.

5. File Validation: Verifies input file existence before processing to avoid errors during encryption or decryption.

6. Output File Handling: Creates output file names dynamically by appending "_encrypted" or "_decrypted" to the original file name.
   
Technologies Used:-
1. Python: Serves as the core language for implementing encryption and utility functionalities.

2. Argparse Module: Enables a user-friendly command-line interface for selecting encryption or decryption actions.

3. Cryptography Library:
-PBKDF2HMAC: Derives secure keys using a password and salt for encryption.
-AES-256: Provides robust encryption to safeguard sensitive files.
-CFB Mode: Ensures encryption works on data of any size without requiring block alignment.

4. OS Module: Handles file validation and generates random salt and IV values for added security.

5. File Handler Utilities: Validates file existence and dynamically generates output file paths with appropriate suffixes.

6. Randomization: Uses secure random generation for salts and initialization vectors to ensure unique encryption for every file.
   
Key Insights:-
AES-256 encryption provides strong security for files, keeping them safe from unauthorized access. Salt and IV (Initialization Vector) help protect the files by making it harder for attackers to spot patterns. It’s important to use a strong and unique password for the best security. File validation ensures that only valid files are encrypted or decrypted, reducing the chances of errors. The naming system for output files prevents overwriting the original files, making the process safer and easier to use.

OUTPUT OF THE TASK:

