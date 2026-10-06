class Car:
    def __init__(self,brand,model,price):
        self.brand = brand
        self.model = model
        self.price = price

C = Car("Toyota", "Fortuner", 4000000)

print("Brand:", C.brand)
print("Model:", C.model)
print("Price:", C.price)