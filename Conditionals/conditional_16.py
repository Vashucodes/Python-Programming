import math

a = float(input("Enter a: "))
b = float(input("Enter b: "))
c = float(input("Enter c: "))

d = b ** 2 - 4 * a * c

if d > 0:
    root1 = (-b + math.sqrt(d)) / (2 * a)
    root2 = (-b - math.sqrt(d)) / (2 * a)
    print("Two real and different roots:", root1, root2)

elif d == 0:
    root = -b / (2 * a)
    print("Two equal roots:", root)

else:
    print("No real roots")