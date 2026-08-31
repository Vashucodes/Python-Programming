n = 5

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if i + j <= n + 1:
            print(chr(j + 64), end="")
        else:
            print(" ", end="")
    print()