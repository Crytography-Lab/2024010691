import math

KEY1 = "APPLE"
KEY2 = "BANANA"

def columnar_transposition_decrypt(cipher, key):
    col_order = sorted(list(enumerate(key)), key=lambda x: x[1])
    col_order = [x[0] for x in col_order]
    
    cols = len(key)
    rows = len(cipher) // cols
    
    matrix = [[''] * cols for _ in range(rows)]
    
    idx = 0
    for col_idx in col_order:
        for row in range(rows):
            if idx < len(cipher):
                matrix[row][col_idx] = cipher[idx]
                idx += 1
            
    plaintext = ""
    for row in range(rows):
        for col in range(cols):
            plaintext += matrix[row][col]
            
    return plaintext

def decrypt(cipher):
    cipher = cipher.replace(" ", "").upper()
    if not cipher:
        return ""
    first_pass_decrypt = columnar_transposition_decrypt(cipher, KEY2)
    second_pass_decrypt = columnar_transposition_decrypt(first_pass_decrypt, KEY1)
    return second_pass_decrypt

if __name__ == "__main__":
    ciphertext = input("Enter ciphertext: ")
    print("Plaintext:", decrypt(ciphertext))
