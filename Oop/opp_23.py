class Employee:
    salary = 234
    _increment = 20

    @property
    def increment(self):
        return self._increment

    @increment.setter
    def increment(self, value):
        self._increment = value

    @property
    def salaryafterincrement(self):
        return self.salary + self.salary * (self._increment / 100)


b = Employee()

print(b.salaryafterincrement)

b.increment = 10

print(b.salaryafterincrement)