numbers = (12,45,33,22,36)

even = 0
odd = 0

for number in numbers:
    if number % 2 == 0:
        even+=1
    else:
        odd+=1

print("Even:",even)
print("ODD:",odd)