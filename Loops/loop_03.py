num = int(input("Enter the number:"))

for i in range(1,num+1):
    if i % 2 == 0:
        print(f"Number is even:{i}")
    else:
        print(f"Number is odd:{i}")