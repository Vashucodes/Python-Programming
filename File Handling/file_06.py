f = open("Text.txt")

d = f.read()

if("twinkle" in d):
    print("find ")
else:
    print("not found")    

f.close()    