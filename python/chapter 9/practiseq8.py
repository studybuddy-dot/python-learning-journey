#create class FoodOrder with item name , quantity , price. Add method to calculate bill

class FoodOrder:
    def __init__(self, item_name, quantity, price):
        self.item_name = item_name
        self.quantity = quantity
        self.price = price

    def calculate_bill(self):
        return self.quantity * self.price

# Example
order1 = FoodOrder("Pizza", 2, 250)
print(order1.calculate_bill())  # Output: 500
