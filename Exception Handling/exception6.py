try:
    a = int(input("Enter the number:"))
    b = int(input("Enter the number:"))
    print(a/b)
except ValueError:
    print("Please enter the number")
except ZeroDivisionError:
    print("Cannot divide by zero")
else:
    print("Division Successful!")
finally:
    print("Program execution completed")