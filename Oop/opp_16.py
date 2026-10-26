class employee:
    company = "ITC"
    name = "Default name"
    def show(self):
        print(f"The name of the employee {self.name} and the comapny is {self.company}")


class coder:
    language  = "Python"
    def printlanguage(self):
        print(f"out of all the language here is your language:{self.language}")

class programmer(employee,coder):
    company = "ITC infotech"
    def showlanguage(self):
        print(f"The name is {self.company} ")

class manager(programmer):
    salary = 120000
    def hold(self):
        print(f"the langauge is {self.language} and salary is {self.salary}")

    

a = employee()
b = programmer()
c = manager()

b.show()
b.printlangauge()
b.showlanguage()
c.hold()