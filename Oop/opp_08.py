class Employee:
    def __init__(self, name, employee_id, salary, department):
        self.name = name
        self.employee_id = employee_id
        self.salary = salary
        self.department = department
        self.bonus = 0

    def display_details(self):
        print(f"Employee Name: {self.name}")
        print(f"Employee ID: {self.employee_id}")
        print(f"Salary: {self.salary}")
        print(f"Department: {self.department}")

    def calculate_bonus(self):
        if self.salary >= 50000:
            self.bonus = self.salary * 0.10
        else:
            self.bonus = self.salary * 0.05

        print(f"Bonus: {self.bonus}")

    def display_total_salary(self):
        total_salary = self.salary + self.bonus
        print(f"Total Salary: {total_salary}")



emp1 = Employee("Aashu", 101, 60000, "IT")


emp1.display_details()
emp1.calculate_bonus()
emp1.display_total_salary()
