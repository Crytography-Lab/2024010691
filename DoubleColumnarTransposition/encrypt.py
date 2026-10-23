import math

KEY1 = "APPLE"
KEY2 = "BANANA"

def columnar_transposition_encrypt(text, key):
    col_order = sorted(list(enumerate(key)), key=lambda x: x[1])
    col_order = [x[0] for x in col_order]
    
    cols = len(key)
    rows = math.ceil(len(text) / cols)
    padded_text = text + "X" * (rows * cols - len(text))
    
    matrix = [padded_text[i:i+cols] for i in range(0, len(padded_text), cols)]
    
    cipher = ""
    for col_idx in col_order:
        for row in range(rows):
            cipher += matrix[row][col_idx]
            
    return cipher

def encrypt(text):
    text = text.replace(" ", "").upper()
    if not text:
        return ""
    first_pass = columnar_transposition_encrypt(text, KEY1)
    second_pass = columnar_transposition_encrypt(first_pass, KEY2)
    return second_pass

if __name__ == "__main__":
    plaintext = input("Enter plaintext: ")
    print("Ciphertext:", encrypt(plaintext))
