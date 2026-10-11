class Student:
    def __init__(self,name,education,roll_no,marks):
        self.name = name
        self.education = education
        self.roll_no = roll_no
        self.marks = marks

    def display(self):
        print(f"Student name :{self.name}")
        print(f"Student education :{self.education}")
        print(f"Student roll no :{self.roll_no}")
        print(f"Student marks: {self.marks}")
    def check_result(self):
        if self.marks >= 40:
            print("Student pass") 
        else:
            print("Student fail")

Info = Student("Aizen","Soul Society",12,34)

Info.display()
Info.check_result()