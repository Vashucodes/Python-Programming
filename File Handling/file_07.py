f = open("Text.txt")


count =0

for line in f:
    count+=1

print("No of line:",count)
f.close()