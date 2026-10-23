# Fixed Key
KEY = 3

def decrypt(text, s):
    result = ""
    for i in range(len(text)):
        char = text[i]
        if char.isupper():
            result += chr((ord(char) - s - 65) % 26 + 65)
        elif char.islower():
            result += chr((ord(char) - s - 97) % 26 + 97)
        else:
            result += char
    return result

if __name__ == "__main__":
    ciphertext = input("Enter ciphertext: ")
    print("Plaintext:", decrypt(ciphertext, KEY))
