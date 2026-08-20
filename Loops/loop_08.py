num = int(input("Enter the number:"))

total = 0
num = abs(num)

while num >0:
    digit = num%10
    total+=digit
    num = num // 10

print(f"Sum of digits:{total}")