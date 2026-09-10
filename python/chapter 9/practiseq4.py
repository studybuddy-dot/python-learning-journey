#create a class student that takes 3 marks and has a method average()

class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks

    def average(self):
        sum=0
        for each in self.marks:
            sum=sum+each
        average=sum/3    
        print("Average is:",average)

student1=Student("Aditya",[90,85,99])
student1.average()
