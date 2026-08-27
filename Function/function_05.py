def sum(n):
    if n ==1:
        return 1
    else:
        return sum(n-1)+n

n = int(input("Enter the number:"))

print(f"Sum :{sum(n)}")