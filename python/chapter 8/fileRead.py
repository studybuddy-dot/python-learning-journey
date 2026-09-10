# 3 ways to read a file
 
# a) Read all file
with open("notes.txt","r") as f:
    data=f.read()
    print(data)

print("--------------------")

# b) Read line by line
with open("notes.txt","r") as f:
    line1=f.readline()
    line2=f.readline()
    line3=f.readline()
    line4=f.readline()
    line5=f.readline()
    print(line1)
    print(line2)
    print(line3)
    print(line4)
    print(line5)


print("-------------------------")

# c) Read all lines
with open("notes.txt","r") as f:
    lines=f.readlines()
    print(lines)