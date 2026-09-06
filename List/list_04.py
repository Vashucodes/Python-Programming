numbers=[]

for i in range(5):
    n = int(input("Enter the number:"))
    numbers.append(n)

largest = numbers[0]
for number in numbers:
    if number > largest:
        largest = number
print("Maximum number in list:",largest)