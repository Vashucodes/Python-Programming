try:
    a = int(input("Enter a number: "))
    print(10 / a)

except ValueError:
    print("Please enter a valid number.")

except ZeroDivisionError:
    print("You cannot divide by zero.")