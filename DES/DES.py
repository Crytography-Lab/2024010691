from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad

text = input("Enter the text: ")
key = input("Enter 8-character key: ")

key = key.encode()
text = text.encode()

cipher = DES.new(key, DES.MODE_ECB)
encrypted = cipher.encrypt(pad(text, DES.block_size))
print("Encrypted:", encrypted.hex())

cipher = DES.new(key, DES.MODE_ECB)
decrypted = unpad(cipher.decrypt(encrypted), DES.block_size)
print("Decrypted:", decrypted.decode())