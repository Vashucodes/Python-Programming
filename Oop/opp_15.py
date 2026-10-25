class employee:
    company = "ITC"

    def show(self):
        print(f"The name of the employee {self.name} and the company is {self.company} ")

class coder:
    language = "Python"
    def printlanguage(self):
        print(f"Your langauge is :{self.language}")
    

class Programmer(employee,coder):
    company = "ITC Infotech"

    def showlanguage(self):
        print(f"The name of the company is {self.company}")


a = employee()
a.name = "Aashu"

b = Programmer()
b.name = "Aizen"


b.show()
b.printlanguage()
b.showlanguage()
