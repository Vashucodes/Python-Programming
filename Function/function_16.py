def fibonacci(n):
    a = 0 
    b = 1
    result = []
    for i in range(n):
        result.append(a)

        c=a+b
        a = b 
        b = c
    return result

n = int(input("Enter the number:"))

print(fibonacci(n))