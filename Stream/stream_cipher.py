text = input("Enter text: ")
key = input("Enter key: ")

if not key:
    print("Key cannot be empty.")
else:
    encrypted = ""

    # Encryption using XOR
    for i in range(len(text)):
        encrypted += chr(ord(text[i]) ^ ord(key[i % len(key)]))

    print("Encrypted text:", encrypted.encode("utf-8").hex())

    # Decryption using XOR
    decrypted = ""

    for i in range(len(encrypted)):
        decrypted += chr(ord(encrypted[i]) ^ ord(key[i % len(key)])))

    print("Decrypted text:", decrypted)
