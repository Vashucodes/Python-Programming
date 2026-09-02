def even_odd(n):
    if n % 2 == 0:
        return "Even"
    else:
        return "Odd"


n = int(input("Enter the number:"))

print(even_odd(n))