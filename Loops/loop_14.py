num = int(input("Enter the number: "))

original = num
temp = num
count = 0
total = 0

# Count the number of digits
while temp != 0:
    count += 1
    temp = temp // 10

# Calculate the Armstrong sum
while num != 0:
    digit = num % 10
    total = total + (digit ** count)
    num = num // 10

# Check if Armstrong
if original == total:
    print("Given number is Armstrong")
else:
    print("Not Armstrong")