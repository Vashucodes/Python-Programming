m = int(input("How many numbers do you want to enter? "))

numbers = set()

for i in range(m):
    n = int(input("Enter the number: "))
    numbers.add(n)

print("Set:", numbers)