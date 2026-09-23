with open("Text.txt") as f:
    content = f.read()

if("python" in content):
    print("Yes Pyhton is present")
else:
    print("no Pyhton is not present")
