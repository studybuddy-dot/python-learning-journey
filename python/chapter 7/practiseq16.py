#create a program using global variable to mmodify a variable from inside a function

x=78
print("Global Before modification",x)

def modify():
    global x
    x=89
    print("Local",x)

modify()
print("Global after modification",x)