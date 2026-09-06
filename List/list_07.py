numbers = [10, 20, 30, 40, 50]

n = int(input("Enter the number:"))

if n in numbers:
    numbers.remove(n)
    print("Updated list:",numbers)
else:
    print("Number not found in the list")

