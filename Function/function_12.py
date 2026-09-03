def sum_of_digits(n):
    total= 0
    while (n != 0):
        r = n % 10
        total = total + r
        n = n // 10 

    return total 

n = int(input("Enter the number:"))

print("Sum of digits",sum_of_digits(n))