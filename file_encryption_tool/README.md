# 🔐 Cryptography File Encryption Tool

A secure, lightweight command-line interface (CLI) utility built in Python using AES-128 symmetric encryption (via the `cryptography` library's Fernet implementation). This tool allows users to easily generate unique encryption keys, encrypt sensitive local files, and decrypt them back to their original state with built-in robust exception handling.

---

## ✨ Features

*   **Symmetric Encryption:** Uses Fernet (AES-128 in CBC mode with HMAC-SHA256) to ensure data confidentiality and integrity.
*   **Robust Error & Exception Handling:** 
    *   Prevents application crashes from empty/missing files.
    *   Detects and warns users if a file has been tampered with or if an incorrect key is used (`InvalidToken` protection).
    *   Gracefully handles accidental user input errors (non-numeric characters in menus) without killing the script.
*   **Zero Hardcoded Paths:** Designed dynamically to execute right out of your local directory on any operating system.
*   **Ready-to-Use Test Suite:** Bundled with sandbox sample data and edge-case blank text files to instantly experiment with the environment safely.

---

## 📦 Prerequisites & Installation

This utility requires **Python 3.x** and the `cryptography` library. Install the required dependency via `pip` before executing the script:

```bash
pip install cryptography
```
---

## 🚀 Usage Guide

### Running the Utility
Launch the application by executing the script in your terminal window:

```bash
python encrypter.py
```

### Navigating the Menu
Upon initialization, you will be greeted by an interactive command menu:

```text
Welcome to File Encryption Tool!

Simple File Encryption Tool
1. Generate Key
2. Encrypt a File
3. Decrypt a File
4. Exit
Enter your choice: 
```

### Step 1: Generate an Encryption Key
Select option `1`. This will create a securely randomized cryptographic key and write it locally as `secret.key`.
> ⚠️ **CRITICAL WARNING:** This file is your absolute recovery mechanism. If you modify, lose, or overwrite `secret.key`, any file encrypted with it will become permanently unrecoverable.

### Step 2: Encrypting a Sample File
Select option `2`. The CLI will prompt you to define your target and destination paths. You can instantly test the flow using the bundled dummy files:
1.  **Enter the file to encrypt:** `input.txt`
2.  **Enter the output file name:** `output.txt`

If you open `output.txt` using a text editor after this operation, you will find its content transformed into a series of unreadable, scrambled cryptographic blocks.

### Step 3: Decrypting an Encrypted File
Select option `3` to reverse the encryption flow:
1.  **Enter the file to decrypt:** `output.txt`
2.  **Enter the output file name:** `restored.txt`

The script will fetch the contents of `secret.key`, verify data integrity, and create a perfectly reconstructed copy of your original text inside `restored.txt`.

---
## 🛠️ Core Script

The entire encryption and decryption logic is contained within the main script. You can view, clone, or modify the source code directly in the repository:

👉 **[View encrypter.py](./encrypter.py)**
```

---

## 🔒 Security Practices & Production Deployment

If you decide to utilize this framework for encrypting legitimate private configurations, personal files, or sensitive information:

1.  **Never Track Real Keys on GitHub:** The `secret.key` committed to this base project repository acts exclusively as a public demo file so that new users don't break on a fresh pull. Do not use this demo key for real files.
2.  **Isolate Production Repositories:** Ensure your local `.gitignore` is completely operational.

Your `.gitignore` file should always contain these directives:
```text
# Block encryption keys from remote tracking
*.key
*.pem

# Block locally restored plain text dumps
restored.txt
```

---

## 📄 License

This project is open-source software licensed under the [MIT License](https://opensource.org/licenses/MIT). Feel free to modify, distribute, and enhance it to suit your workflow needs.