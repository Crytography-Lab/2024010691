a = int(input("Enter a: "))
b = int(input("Enter b: "))
n = int(input("Enter n: "))

if (a - b) % n == 0:
    print(a, ",", b, "are congruent")
else:
    print(a, ",", b, "are not congruent")
