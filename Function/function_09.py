def greatest(a, b, c):

    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    else:
        return c


a = 3
b = 89
c = 56

print(greatest(a, b, c))