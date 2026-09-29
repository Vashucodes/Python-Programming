try:
    a = int(input("Enter the number:"))
    b = int(input("Enter the number:"))
    print(a/b)
except ZeroDivisionError:
    print("Cannot divide by zero")
else:
    print("Division Successful!")