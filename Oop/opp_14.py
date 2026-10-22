class Employee:
    company = "ITC"

    def show(self):
        print(f"The name is {self.name} and the salary is {self.salary}")


class Programmer(Employee):
    company = "ITC Infotech"

    def showlanguage(self):
        print(
            f"The name is {self.name} and "
            f"he is good with {self.language} language"
        )


a = Employee()
b = Programmer()

a.name = "Aashu"
a.salary = 30000

b.name = "Aizen"
b.salary = 50000
b.language = "Python"

print(a.company, b.company)

a.show()
b.show()
b.showlanguage()
