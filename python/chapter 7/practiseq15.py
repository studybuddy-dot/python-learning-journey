#write a program with local variable score inside a function and one global outside

a=int(input("Enter the global variable:"))


def show():
    a=int(input("Enter the local variable:"))
    print("This is the local variable:",a)
show()

print("This is the global variable:",a)