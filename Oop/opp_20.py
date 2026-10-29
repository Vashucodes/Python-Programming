class number:
    def __init__(self,n):
        self.n = n

    def __add__(self,num):
        return self.n + self.n
n= number(4)
m= number(3)

print(n+m)