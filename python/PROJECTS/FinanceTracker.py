#Expense tracker project
expenseList = [] #list as dictionary
print("Welcome to Expense Tracker!")

while True:
    print("====MENU====")
    print("1.Add expense")
    print("2.View all spending")                                       
    print("3.View total spending")
    print("4.Exit")

    choice=int(input("Please enter your choice(1:4): "))

#1 ADD expense

    if(choice==1):
        date=input("Date: ")
        category=input("Category: ")
        description=input("Description: ")
        amount=int(input("Amount: "))

        expense={
            "date":date,
            "category":category,
            "description":description,
            "amount":amount
        } 
        
        expenseList.append(expense)
        print("Expense added successfully!")

#2 VIEW all spending

    elif(choice==2):
        if(len(expenseList)==0):
            print("No expenses added!")
        else:
            print("===TOTAL SPENDING===")    
            count = 1 
            for eachspending in expenseList:
                print(f"Spending{count} -> {eachspending["date"]} , {eachspending["category"]} , {eachspending["description"]} , {eachspending["amount"]} " )
                count=count+1

#3 VIEW total spending
    elif(choice==3):
        total=0
        for eachspending in expenseList:
            total = total + eachspending["amount"]
            print("Total spending=",total)

#4 EXIT
    elif(choice==4):
        print("Thank you for using Expense Tracker!Byee Byee<33")
        break

#other invalid choice
    else:
        print("Invalid choice!Try again")
