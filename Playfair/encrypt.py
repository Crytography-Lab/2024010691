KEY = "MONARCHY"

def create_matrix(key):
    key = key.upper().replace("J", "I")
    matrix = []
    seen = set()
    for char in key + "ABCDEFGHIKLMNOPQRSTUVWXYZ":
        if char not in seen and char.isalpha():
            seen.add(char)
            matrix.append(char)
    return [matrix[i:i+5] for i in range(0, 25, 5)]

def find_position(matrix, char):
    for i, row in enumerate(matrix):
        for j, c in enumerate(row):
            if c == char:
                return i, j
    return None

def prepare_text_encrypt(text):
    text = text.upper().replace("J", "I")
    text = ''.join(filter(str.isalpha, text))
    res = ""
    i = 0
    while i < len(text):
        res += text[i]
        if i + 1 < len(text) and text[i] == text[i+1]:
            res += "X"
        elif i + 1 < len(text):
            res += text[i+1]
            i += 1
        i += 1
    if len(res) % 2 != 0:
        res += "X"
    return res

def encrypt(text):
    matrix = create_matrix(KEY)
    text = prepare_text_encrypt(text)
    result = ""
    for i in range(0, len(text), 2):
        r1, c1 = find_position(matrix, text[i])
        r2, c2 = find_position(matrix, text[i+1])
        if r1 == r2:
            result += matrix[r1][(c1 + 1) % 5] + matrix[r2][(c2 + 1) % 5]
        elif c1 == c2:
            result += matrix[(r1 + 1) % 5][c1] + matrix[(r2 + 1) % 5][c2]
        else:
            result += matrix[r1][c2] + matrix[r2][c1]
    return result

if __name__ == "__main__":
    plaintext = input("Enter plaintext: ")
    print("Ciphertext:", encrypt(plaintext))
