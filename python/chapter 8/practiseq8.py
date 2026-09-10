#print how many lines are there in a file

with open("notes.txt","r") as f:
    lines=f.readlines()
    print(len(lines))