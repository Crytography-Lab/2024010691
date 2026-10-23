import string

KEY = "QWERTYUIOPASDFGHJKLZXCVBNM"
alphabet = string.ascii_uppercase

def decrypt(text):
    text = text.upper()
    result = ""
    for char in text:
        if char in KEY:
            idx = KEY.index(char)
            result += alphabet[idx]
        else:
            result += char
    return result

if __name__ == "__main__":
    ciphertext = input("Enter ciphertext: ")
    print("Plaintext:", decrypt(ciphertext))
