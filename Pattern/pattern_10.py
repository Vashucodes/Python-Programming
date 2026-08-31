n = 5
for i in range(1,n+1):
    for j in range(1,n+1):
        if i == 3 or j == 3 :
            print("*",end="")
        else:
            print(" ",end="")
    print()