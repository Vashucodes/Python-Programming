def count_digits(n):
    count =0
    while n != 0:
        count +=1
        n = n // 10

    return count


n = int(input("Enter the number:"))

print("Number of digist:",count_digits(n))
