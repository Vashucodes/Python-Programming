n = 5
for i in range(1,n+1):
    for j in range(1,n+1):
        if i+j >= 6:
            print("*",end="")
        else:
            print(" ",end="")
    print()