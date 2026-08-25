base = int(input("Enter base:"))
expo = int(input("Enter expo:"))
p = 1
for i in range(1,expo+1):
    p = p * base
print(f"The power of given number : {p}")