num = int(input("Enter the number:"))

i=1
fact = 1
while i<=num:
    fact*=i
    i+=1

print(f"Factorial is : {fact}")