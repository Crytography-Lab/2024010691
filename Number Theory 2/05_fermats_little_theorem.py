def prime(a):
    for i in range(2, int(a**0.5) + 1):
        if a % i == 0:
            return False
    return True


a = int(input("Enter a: "))
p = int(input("Enter p: "))

if prime(p) and a % p != 0:
    print(a, "^", (p - 1), "is congruent to 1 modulo", p)
else:
    print(a, "^", (p - 1), "is not congruent to 1 modulo", p)
