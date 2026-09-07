numbers = [10, 20, 30, 40, 50]

n = int(input("Enter the number:"))

if n  in numbers:
    print("Index:",numbers.index(n))
else:
    print("Element not found")
    