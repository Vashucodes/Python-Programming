numbers  = []

for i in range(5):
    n = int(input("Enter the number:"))
    numbers.append(n)


total = 0

for number in numbers:
    total+=number

print(numbers)
print("Sum of all element in list:",total)