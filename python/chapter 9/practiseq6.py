#create class student with name,section and marks. Add method get_percentage()

class Student():
    def __init__(self,name,section,marks):
        self.name = name
        self.section = section
        self.marks = marks

    def get_percentage(self):
        return(sum(self.marks)/len(self.marks)) if self.marks else 0

s1=Student("Alice","10th",[95,80,99])
print(s1.get_percentage())