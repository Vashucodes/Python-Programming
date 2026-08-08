n1 = float(input("Enter the first number: "))
operator = input("Enter the operator (+, -, *, /): ")
n2 = float(input("Enter the second number: "))

if operator == "+":
    print("Result:", n1 + n2)
elif operator == "-":
    print("Result:", n1 - n2)
elif operator == "*":
    print("Result:", n1 * n2)
elif operator == "/":
    if n2 != 0:
        print("Result:", n1 / n2)
    else:
        print("Cannot divide by zero")
else:
    print("Invalid operator")