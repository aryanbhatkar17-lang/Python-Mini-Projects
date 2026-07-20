from cryptography.fernet import Fernet, InvalidToken

def generate_key():
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)
    print("Key generated and saved in 'secret.key' file. Keep it safe!")


def decrypt_file(input_file, output_file):
    # FIX 1: Removed the hardcoded '/home/chef/workspace/' path so it works on any machine
    try:
        with open("secret.key", "rb") as key_file:
            key = key_file.read()
        cipher = Fernet(key)
    except FileNotFoundError:
        print("Error: 'secret.key' not found. You need the original key to decrypt!")
        return

    # FIX 2: Added error handling for missing files or wrong/corrupted keys
    try:
        with open(input_file, "rb") as file:
            encrypted_data = file.read()
        
        decrypted_data = cipher.decrypt(encrypted_data)
        
        with open(output_file, "wb") as file:
            file.write(decrypted_data)
        
        print(f"File '{input_file}' decrypted successfully into '{output_file}'!")
    except FileNotFoundError:
        print(f"Error: The input file '{input_file}' could not be found.")
    except InvalidToken:
        print("Error: Decryption failed! The key is invalid or the file is corrupted.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


def encrypt_file(input_file, output_file):
    # FIX 3: Split the try-except blocks so missing files don't falsely blame the secret key
    try:
        with open("secret.key", "rb") as key_file:
            key = key_file.read()
        cipher = Fernet(key)
    except FileNotFoundError:
        print("Error: 'secret.key' not found! GENERATE SECRET KEY FIRST (Option 1).")
        return

    try:
        with open(input_file, "rb") as file:
            file_data = file.read()

        encrypted_data = cipher.encrypt(file_data)
        
        with open(output_file, "wb") as file:
            file.write(encrypted_data)
        
        print(f"File '{input_file}' encrypted successfully into '{output_file}'!")
    except FileNotFoundError:
        print(f"Error: The input file '{input_file}' could not be found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


def user_choice():
    while True:
        print("\nSimple File Encryption Tool")
        print("1. Generate Key")
        print("2. Encrypt a File")
        print("3. Decrypt a File")
        print("4. Exit")
        
        # FIX 4: Wrapped input in a try-except block to prevent crashes if a user types letters
        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input! Please enter a valid number (1-4).")
            continue
        
        if choice == 1:
            generate_key()
        elif choice == 2:
            input_file = input("Enter the file to encrypt: ")
            output_file = input("Enter the output file name: ")
            encrypt_file(input_file, output_file)
        elif choice == 3:
            input_file = input("Enter the file to decrypt: ")
            output_file = input("Enter the output file name: ")
            decrypt_file(input_file, output_file)
        elif choice == 4:
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice! Please select a number between 1 and 4.")

if __name__ == "__main__":
    print("Welcome to File Encryption Tool!\n")
    user_choice()