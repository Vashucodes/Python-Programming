try:
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))
    print("Division =", a / b)

except ZeroDivisionError:
    print("Cannot divide by zero")

except ValueError:
    print("Please enter a valid number")

finally:
    print("Program execution completed")