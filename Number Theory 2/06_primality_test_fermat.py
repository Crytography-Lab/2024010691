a = int(input("Enter a: "))
p = int(input("Enter p: "))

if ((a**(p - 1) - 1) % p == 0):
    print(p, "is probably prime")
else:
    print(p, "is composite")
