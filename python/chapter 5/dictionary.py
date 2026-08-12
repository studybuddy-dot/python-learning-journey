#creating dictionary 
student = {
    "name" : "sanyukta joshi",
    "age" : 21,
    "city" : "Pune"
}

#accessing elements
print(student["age"])

#prinitng type of data
print(type(student))

#duplicate keys does not create an error but prints last duplicate key

#adding or updating elements
student["college"]="NMIET"  #add
student["age"]="22" #update
print(student)

#removing items
student.pop("college")
print(student)