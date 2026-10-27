class employee:
    def __init__(self):
        print("Constructor of employee")
        self.a = 1

class  programmer(employee):
    def __init__(self):
        super().__init__()
        print("Constructor of programmer ")
        self.b = 2

class manager(programmer):
    def __init__(self):
        super().__init__()
        print("Constructor of manager")
        self.c = 3

o = manager()
print(o.a,o.b,o.c)
