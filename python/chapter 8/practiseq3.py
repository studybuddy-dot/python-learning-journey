#what happens if u try to open a nonexisting file in r mode?

file=open("notes.txt","r")
data=file.read()
print(data)

#error occurs