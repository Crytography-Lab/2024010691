KEY_MATRIX = [[3, 3], [2, 5]]

def encrypt(text):
    text = text.upper().replace(" ", "")
    text = ''.join(filter(str.isalpha, text))
    if len(text) % 2 != 0:
        text += "X"
        
    result = ""
    for i in range(0, len(text), 2):
        x = ord(text[i]) - 65
        y = ord(text[i+1]) - 65
        
        c1 = (KEY_MATRIX[0][0] * x + KEY_MATRIX[0][1] * y) % 26
        c2 = (KEY_MATRIX[1][0] * x + KEY_MATRIX[1][1] * y) % 26
        
        result += chr(c1 + 65) + chr(c2 + 65)
    return result

if __name__ == "__main__":
    plaintext = input("Enter plaintext: ")
    print("Ciphertext:", encrypt(plaintext))
