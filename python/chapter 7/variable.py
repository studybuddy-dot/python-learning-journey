#local and global variable

x=10 #global variable

def show():
    x=5 #local variable
    print("Inside function:",x)

show()

print("Outside function:",x)