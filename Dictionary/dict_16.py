marks = {
    "Math": 80,
    "Python": 90,
    "COA": 75,
    "Java": 85
} 
even = 0
odd = 0
for subject,mark in marks.items():
    if mark % 2 == 0:
        even+=1
    else:
        odd+=1

print("Even:",even)
print("Odd:",odd)