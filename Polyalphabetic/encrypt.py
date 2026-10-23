KEY = "SECRET"

def encrypt(text, key):
    result = ""
    key_idx = 0
    text = text.upper()
    key = key.upper()
    
    for char in text:
        if char.isalpha():
            shift = ord(key[key_idx % len(key)]) - 65
            result += chr((ord(char) + shift - 65) % 26 + 65)
            key_idx += 1
        else:
            result += char
    return result

if __name__ == "__main__":
    plaintext = input("Enter plaintext: ")
    print("Ciphertext:", encrypt(plaintext, KEY))
