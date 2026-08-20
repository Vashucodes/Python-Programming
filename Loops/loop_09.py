num = int(input("Enter the number:"))


rev = 0
while num > 0:
    digit = num%10
    rev = rev *10 + digit
    num = num // 10

print(f"Reverse number is :{rev}")