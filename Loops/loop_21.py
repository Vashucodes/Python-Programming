n = int(input("Enter the number:"))

sum = 0
for i in range(1,n+1):
    sum = sum + i
    print(i ,end="")
print(f" The Sum of all natural number from 1 to n:{sum}")