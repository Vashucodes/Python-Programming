
class ShoppingCart:
    def __init__(self):
        self.items = {}

    def add_item(self, name, price, quantity):
        if price <= 0 or quantity <= 0:
            print("Price and quantity must be positive!")
            return

        if name in self.items:
            self.items[name]["quantity"] += quantity
            self.items[name]["price"] = price
        else:
            self.items[name] = {
                "price": price,
                "quantity": quantity
            }

        print(f"{name} added to cart successfully!")

    def remove_item(self, name):
        if name in self.items:
            del self.items[name]
            print(f"{name} removed from cart!")
        else:
            print(f"{name} not found in cart!")

    def display_cart(self):
        if not self.items:
            print("Shopping cart is empty!")
            return

        print("\nShopping Cart:")

        for name, details in self.items.items():
            print(
                f"{name} - Price: {details['price']}, "
                f"Quantity: {details['quantity']}"
            )

    def calculate_total(self):
        total = 0

        for details in self.items.values():
            total += details["price"] * details["quantity"]

        print(f"Total Bill: {total}")



cart = ShoppingCart()

cart.add_item("Laptop", 50000, 1)
cart.add_item("Mouse", 500, 2)
cart.add_item("Keyboard", 1500, 1)


cart.display_cart()
cart.calculate_total()

cart.remove_item("Mouse")


print("\nAfter removing Mouse:")
cart.display_cart()
cart.calculate_total()
