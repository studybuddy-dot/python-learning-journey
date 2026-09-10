#defualt constructor

class Student:
    Clgname="Abc clg"
    def __init__(self,name,course):
        print("I get called automatically when an object is created")
        self.name=name
        self.course=course
        print(self.name)
        print(self.course)

s1=Student("A","Btech")
print("Name of student 1 is:",s1.name)
print("Course of student 1 is:",s1.course)
s2=Student("B","BCs")
print("Name of student 2 is:",s2.name)
print("Course of student 2 is:",s2.course)