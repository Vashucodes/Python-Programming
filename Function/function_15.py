def is_armstrong(n):
    original = n
    total = 0
    digits = len(str(n))

    while n != 0:
        r = n % 10 
        total = total + r ** digits
        n = n // 10 

    return original == total


n = int(input("Enter the number:"))

print(is_armstrong(n))