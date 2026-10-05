class Rectangle:
    length = 5
    width = 10

R = Rectangle()

area = R.length * R.width
perimeter = 2 * (R.length + R.width)

print("Area of rectangle:", area)
print("Perimeter of rectangle:", perimeter)