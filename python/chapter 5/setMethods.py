#methods in sets
employee={"name","salary","empID","age"}
manager={"name","age","salary","domain","qualification"}
employee.add("skills")
print(employee)
manager.remove("age")
print(manager)
print(employee.union(manager))
print(employee.intersection(manager))
employee.pop()
print(employee)
#manager.clear()        clears whole set
#print(manager)         output = set()