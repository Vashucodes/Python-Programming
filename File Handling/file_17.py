with open("note.txt") as f:
    data = f.read()
with open("note_rename.txt","w") as f:
    f.write(data)