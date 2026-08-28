def parameter():
    centimeter = inches * 2.54
    return centimeter

inches = int(input("Enter the number:"))
print(f"The corresponding value of centimeter is :{parameter()}")