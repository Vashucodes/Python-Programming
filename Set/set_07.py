numbers = {10,20,33,43,23,22}

n = int(input("Enter the number:"))

if n in numbers:
    numbers.discard(n)
    print(numbers)
else:
    print("Number not found")