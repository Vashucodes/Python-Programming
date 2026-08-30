n = 5

for i in range(1, n + 1):
    for j in range(1, 2 * n):
        if j >= n - i + 1 and j <= n + i - 1:
            print(j, end="")
        else:
            print(" ", end="")
    print()