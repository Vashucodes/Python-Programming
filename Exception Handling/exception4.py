try:
    a = 100
    b = int(input("Enter the number:"))
    print(a/b)
except ZeroDivisionError:
    print("Cannot divide by zero")
finally:
    print("Program execution completed")