p = int(input("Enter p: "))
q = int(input("Enter q: "))

n = p * q
phi = (p - 1) * (q - 1)

e = 2
while e < phi:
    a = 1
    while (e * a) % phi != 1:
        a += 1
    if a > 1:
        break
    e += 1

d = a

m = int(input("Enter message: "))

c = pow(m, e, n)
print("Encrypted:", c)

m2 = pow(c, d, n)
print("Decrypted:", m2)