with open("text.txt") as f:
    content = f.read()

with open("text_copy.txt","w") as f:
    f.write(content)