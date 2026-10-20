class calculator:
    def __int__(self,n):
        self.n = n

    def square(self):{
        print(f"The square is : {self.n}*{self.n}")
    }
    def cube(self):{
        print(f"The cube is : {self.n}*{self.n}*{self.n}")
    }
    def squareroot(self):{
        print(f"The square is : {self.n**0.5}")
    }
    @staticmethod # is used when a method does not need self or the instance.
    def greet():
        print("Hello")
a = calculator(8)
a.square()
a.cube()
a.squareroot()
a.greet()
        