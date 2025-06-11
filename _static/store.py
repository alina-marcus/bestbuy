class Product:

    def __init__(self, name, price, quantity):
        if not name:
            raise ValueError("Product name is required")
        if quantity < 0:
            raise ValueError("Quantity must be positive")

        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True

    def get_quantity(self):
        return self.quantity

    def set_quantity(self, quantity):
        self.quantity = quantity
        if self.quantity == 0:
            self.active = False

    def is_active(self):
        return self.active

    def activate(self):
        self.active = True

    def deactivate(self):
        self.active = False

    def show(self):
        return f"{self.name}, Price: {self.price}, Quantity: {self.quantity}"

    def buy(self, quantity_bought):
        if quantity_bought > self.quantity:
            return "Not enough stock available"
        if self.quantity == 0 or not self.active:
            return "This product is not available"

        self.quantity -= quantity_bought
        self.set_quantity(self.quantity)
        total_price = self.price * quantity_bought
        return f"Great choice! You bought {self.name} x {quantity_bought}. Total price: {self.price * quantity_bought}"

# Test
bose = Product("Bose QuietComfort Earbuds", price=250, quantity=500)
mac = Product("MacBook Air M2", price=1450, quantity=100)

print(bose.buy(50))
print(mac.buy(100))
print(mac.is_active())

bose.show()
print(mac.show())

bose.set_quantity(1000)
print(bose.show())