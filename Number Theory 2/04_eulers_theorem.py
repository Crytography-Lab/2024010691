def gcd(a, b):
    r = b
    while r != 0:
        q = a // b
        r = a % b
        a = b
        b = r
    return a


a = int(input("Enter a: "))
n = int(input("Enter n: "))

c = 0

for i in range(1, n):
    if gcd(n, i) == 1:
        c += 1
    else:
        continue

if gcd(a, n) == 1:
    print(a, "^", c, "is congruent to 1 modulo", n)
else:
    print("Can't apply ET: gcd(a,n) != 1")
