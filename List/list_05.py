numbers =[2,3,45,65,7]

even = 0
odd = 0

for number in numbers:
    if number % 2 == 0:
        even+=1
    else:
        odd+=1

print("Even number in list is:",even)
print("Odd number in list is:",odd)