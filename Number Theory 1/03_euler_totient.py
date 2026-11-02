def gcd(a, b):
    r = b
    while r != 0:
        q = a // b
        r = a % b
        a = b
        b = r
    return a


n = int(input("Enter n: "))
c = 0

for i in range(1, n):
    if gcd(n, i) == 1:
        c += 1
    else:
        continue

print("Euler Totient:", c)
