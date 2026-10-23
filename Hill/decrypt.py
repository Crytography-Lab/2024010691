INV_KEY_MATRIX = [[15, 17], [20, 9]]

def decrypt(text):
    text = text.upper().replace(" ", "")
    text = ''.join(filter(str.isalpha, text))
    if len(text) % 2 != 0:
        text += "X"
        
    result = ""
    for i in range(0, len(text), 2):
        x = ord(text[i]) - 65
        y = ord(text[i+1]) - 65
        
        p1 = (INV_KEY_MATRIX[0][0] * x + INV_KEY_MATRIX[0][1] * y) % 26
        p2 = (INV_KEY_MATRIX[1][0] * x + INV_KEY_MATRIX[1][1] * y) % 26
        
        result += chr(p1 + 65) + chr(p2 + 65)
    return result

if __name__ == "__main__":
    ciphertext = input("Enter ciphertext: ")
    print("Plaintext:", decrypt(ciphertext))
