from pathlib import Path
from Crypto.Cipher import AES
import os

def get_key():
  while True:
    key = input("Enter a 16-byte encryption key: ")
    if len(key) == 16:
      return key.encode()
    else:
      print("Error: Key must be 16 bytes long. Please try again.")

def get_file_extension():
  while True:
    extension = input("Enter the file extension to encrypt (e.g., .docx, .pdf): ")
    if extension.startswith('.'):
      return extension
    else:
      print("Error: Extension must start with a dot (.)")

def pad_data(data):
  padding_length = 16 - (len(data) % 16)
  return data + bytes([padding_length] * padding_length)

def unpad_data(data):
  padding_length = data[-1]
  return data[:-padding_length]

def encrypt_file(path, key):
  with open(str(path), 'rb') as f:
    data = f.read()
  data = pad_data(data)
  iv = os.urandom(16)
  cipher = AES.new(key, AES.MODE_CBC, iv)
  encrypted_data = cipher.encrypt(data)
  with open(str(path) + ".encrypted", 'wb') as f:
    f.write(iv + encrypted_data)
  os.remove(str(path))

def decrypt_file(path, key):
  with open(str(path), 'rb') as f:
    data = f.read()
  iv = data[:16]
  encrypted_data = data[16:]
  cipher = AES.new(key, AES.MODE_CBC, iv)
  decrypted_data = cipher.decrypt(encrypted_data)
  decrypted_data = unpad_data(decrypted_data)
  with open(str(path)[:-len(".encrypted")], 'wb') as f:
    f.write(decrypted_data)
  os.remove(str(path))

def get_files(directory, extension):
  paths = list(Path(directory).rglob("*" + extension))
  return paths

def main():
  
  key = get_key()

  
  mode = input("Enter 'e' to encrypt or 'd' to decrypt: ").lower().rstrip()
  if mode not in ('e', 'd'):
    print("Invalid choice. Please enter 'e' or 'd'.")
    return

  directory = input("Enter the directory path: ").rstrip()
  print("Selected directory:", directory)

  if mode == 'e':
    extension = get_file_extension()
    paths = get_files(directory, extension)

    print("Selected files:")
    for path in paths:
      print(path)

    confirmation = input("Are you sure you want to encrypt these files? (y/n): ").lower().rstrip()
    if confirmation == 'y':
      for path in paths:
        encrypt_file(path, key)
      print("Files encrypted successfully!")
    else:
      print("Encryption cancelled.")
  else:
    extension = input("Enter the file extension of encrypted files (e.g., .docx.encrypted): ")
    paths = get_files(directory, extension)

    print("Selected encrypted files:")
    for path in paths:
      print(path)

    confirmation = input("Are you sure you want to decrypt these files? (y/n): ").lower().rstrip()
    if confirmation == 'y':
        for path in paths:
            decrypt_file(path,key)
        print("Files decrypted successfully!")
    else:
      print("Decryption Cancelled!")


main()