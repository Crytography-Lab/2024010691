import math

p = int(input("Enter p: "))
q = int(input("Enter q: "))

n = p * q
phi = (p - 1) * (q - 1)

e = 2
while math.gcd(e, phi) != 1:
    e += 1

d = pow(e, -1, phi)

m = int(input("Enter message: "))

c = pow(m, e, n)
print("Encrypted:", c)

m2 = pow(c, d, n)
print("Decrypted:", m2)