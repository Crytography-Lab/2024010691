
p = int(input("Enter prime number p: "))
g = int(input("Enter generator g: "))

a = int(input("Enter private key of Alice: "))
b = int(input("Enter private key of Bob: "))

A = pow(g, a, p)
B = pow(g, b, p)

print("Alice's public key:", A)
print("Bob's public key:", B)

key1 = pow(B, a, p)
key2 = pow(A, b, p)

print("Alice's shared key:", key1)
print("Bob's shared key:", key2)

if key1 == key2:
    print("Shared key established successfully")
else:
    print("Key exchange failed")
