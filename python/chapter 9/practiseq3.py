#create a class fooditem with class attribute category = "snacks" and instance attribute name "samosa" , "gulabjamun" 

class FoodItem:
    category="Snacks"
    def __init__(self,name):
        self.name=name

snack1=FoodItem("Samosa")
print(snack1.name)
snack2=FoodItem("Gulabjamun")
print(snack2.name)