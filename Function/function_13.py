def reverse(n):
    rev = 0
    while n != 0:
        r = n % 10
        rev = rev * 10 + r
        n = n // 10
    return rev 


n = int(input("Enter the number:"))

print("Reverse :",reverse(n))