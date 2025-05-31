import base64
import os
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

def encrypt(raw, key):
    raw = pad(raw.encode(), 16)
    iv = os.urandom(16)  
    cipher = AES.new(key.encode('utf-8'), AES.MODE_CBC, iv)
    encrypted = cipher.encrypt(raw)
    return base64.b64encode(iv + encrypted)  

def decrypt(enc, key):
    enc = base64.b64decode(enc)
    iv = enc[:16]  
    ciphertext = enc[16:]  
    cipher = AES.new(key.encode('utf-8'), AES.MODE_CBC, iv)
    return unpad(cipher.decrypt(ciphertext), 16)

# Input data and key
data = input("Enter the data to encrypt: ")
key = input("Enter the encryption key (16 characters): ")

# Ensure key is 16 characters long
if len(key) != 16:
    print("Key must be 16 characters long.")
else:
    encrypted = encrypt(data, key)
    print('Encrypted:', encrypted.decode("utf-8", "ignore"))

    decrypted = decrypt(encrypted, key)
    print('Decrypted data:', decrypted.decode("utf-8", "ignore"))
