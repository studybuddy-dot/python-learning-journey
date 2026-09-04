#default arguments

def greet(name="sany"):
    print("hello!",name)

greet()
greet("riya")

#keyword arguments

def student_info(name,age):
    print(name,"is",age,"years old")

student_info(name="sany",age=20)