#create a class laptop with attributes brand , ram and price . Create 2 objects with different values

class Laptop:
    brand="dell"
    RAM="8GB"
    price="1lakh"

laptop1=Laptop()
laptop1.brand="Macbook"
print("Brand of Laptop 1 is",laptop1.brand)
laptop1.price="2lakh"
print("Price of Laptop 1 is",laptop1.price)
laptop1.RAM="16GB"
print("RAM of Laptop 1 is",laptop1.RAM)

laptop2=Laptop()
laptop2.brand="Lenovo"
print("Brand of Laptop 2 is",laptop2.brand)
laptop2.price="60k"
print("Price of Laptop 2 is",laptop2.price)
laptop2.RAM="4GB"
print("RAM of Laptop 2 is",laptop2.RAM)
