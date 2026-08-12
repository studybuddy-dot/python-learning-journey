#bill split calculator
bill = float(input("Enter total bill: "))
ppl = int(input("Enter number of people: "))
contri = bill / ppl
print("Contri for each person is: ", contri)
print("Datatype of variables are:")
print("bill" , type(bill))
print("ppl" , type(ppl))      
print("contri" , type(contri)) 