def rc4(key, text):
    S = list(range(256))
    j = 0

    # Key Scheduling Algorithm (KSA)
    for i in range(256):
        j = (j + S[i] + ord(key[i % len(key)])) % 256
        S[i], S[j] = S[j], S[i]

    # Pseudo-Random Generation Algorithm (PRGA)
    i = 0
    j = 0
    result = ""

    for char in text:
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        S[i], S[j] = S[j], S[i]

        k = S[(S[i] + S[j]) % 256]
        result += chr(ord(char) ^ k)

    return result


key = input("Enter key: ")
text = input("Enter text: ")

if not key:
    print("Key cannot be empty.")
else:
    encrypted = rc4(key, text)
    print("Encrypted text:", encrypted.encode("utf-8").hex())

    decrypted = rc4(key, encrypted)
    print("Decrypted text:", decrypted)
