def fact(n):
    if n ==1 or n == 0:
        return 1
    return fact(n-1)*n

n = int(input("Enter the number:"))
print(f"Factorial :{fact(n)}")