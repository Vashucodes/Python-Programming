a = int(input("Enter the number:"))

for i in range(1,a+1):
    if a % i == 0:
        print(f"Factor: {i} ",end="")