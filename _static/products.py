class Product:
    """
    Represents a product in an inventory system.

    Attributes:
        name (str): The name of the product.
        price (float): The price per unit of the product.
        quantity (int): The quantity of the product in stock.
        active (bool): Indicates whether the product is available for purchase.
    """

    def __init__(self, name, price, quantity):
        """
        Initializes a new Product instance.

        Args:
            name (str): The name of the product.
            price (float): The price per unit.
            quantity (int): The number of items available.

        Raises:
            ValueError: If name is empty or quantity is negative.
        """
        if not name:
            raise ValueError("Product name is required")
        if quantity < 0:
            raise ValueError("Quantity must be positive")

        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True

    def get_quantity(self):
        """
        Returns the current quantity of the product.

        Returns:
            int: The quantity in stock.
        """
        return self.quantity

    def set_quantity(self, quantity):
        """
        Updates the quantity of the product and deactivates it if quantity reaches zero.

        Args:
            quantity (int): The new quantity.
        """
        self.quantity = quantity
        if self.quantity == 0:
            self.active = False

    def is_active(self):
        """
        Checks if the product is active and available for purchase.

        Returns:
            bool: True if active, False otherwise.
        """
        return self.active

    def activate(self):
        """
        Activates the product, making it available for purchase.
        """
        self.active = True

    def deactivate(self):
        """
        Deactivates the product, making it unavailable for purchase.
        """
        self.active = False

    def show(self):
        """
        Returns a string representation of the product.

        Returns:
            str: Formatted string with name, price, and quantity.
        """
        return f"{self.name}, Price: {self.price}, Quantity: {self.quantity}"

    def buy(self, quantity_bought):
        """
        Processes a purchase of the product.

        Args:
            quantity_bought (int): The quantity the customer wants to buy.

        Returns:
            float or str: The total price if successful, or an error message.
        """
        if quantity_bought > self.quantity:
            return "Not enough stock available"
        if self.quantity == 0 or not self.active:
            return "This product is not available"

        self.quantity -= quantity_bought
        self.set_quantity(self.quantity)
        total_price = self.price * quantity_bought
        return total_price
