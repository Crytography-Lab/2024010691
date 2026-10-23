import string

KEY = "QWERTYUIOPASDFGHJKLZXCVBNM"
alphabet = string.ascii_uppercase

def encrypt(text):
    text = text.upper()
    result = ""
    for char in text:
        if char in alphabet:
            idx = alphabet.index(char)
            result += KEY[idx]
        else:
            result += char
    return result

if __name__ == "__main__":
    plaintext = input("Enter plaintext: ")
    print("Ciphertext:", encrypt(plaintext))
