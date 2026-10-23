from cryptography.fernet import Fernet

key = Fernet.generate_key()
cipher = Fernet(key)

text = input("Enter text: ")

encrypted = cipher.encrypt(text.encode())
print("Encrypted:", encrypted.decode())

decrypted = cipher.decrypt(encrypted).decode()
print("Decrypted:", decrypted)