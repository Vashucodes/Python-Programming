a = int(input("Enter the number:"))
last = a % 10
while a != 0:
    r = a % 10
    a = a // 10
print(f"The first digit is :{r} and last digit : {last}")