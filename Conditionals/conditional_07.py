marks = int(input("Enter your marks: "))

if marks < 0 or marks > 100:
    print("Invalid Marks")

elif marks >= 90:
    print("Grade Ex")

elif marks >= 80:
    print("Grade A")

elif marks >= 70:
    print("Grade B")

elif marks >= 60:
    print("Grade C")

elif marks >= 50:
    print("Grade D")

else:
    print("Grade F")