marks = {
    "Math": 80,
    "Python": 90,
    "COA": 75,
    "Java": 85
} 

hightest = 0
subject_name = ""

for subject,mark in marks.items():
    if mark > hightest:
        hightest = mark
        subject_name = subject

print("Hightest:",hightest,subject_name)