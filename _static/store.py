import products


class Store:
    """
    Represents a store containing a list of products.

    Attributes:
        products (list): A list of Product instances available in the store.
    """

    def __init__(self, products=None):
        """
        Initializes the Store with an optional list of products.

        Args:
            products (list, optional): List of Product instances. Defaults to empty list.
        """
        if products is None:
            products = []
        self.products = products

    def add_product(self, product):
        """
        Adds a product to the store's inventory.

        Args:
            product (Product): The product to add.
        """
        self.products.append(product)

    def remove_product(self, product):
        """
        Removes a product from the store's inventory.

        Args:
            product (Product): The product to remove.
        """
        self.products.remove(product)

    def get_total_quantity(self):
        """
        Returns the total number of unique products in the store.

        Returns:
            int: Count of unique products.
        """
        return len(self.products)

    def get_all_products(self):
        """
        Retrieves all active products available in the store.

        Returns:
            list: List of active Product instances.
        """
        active_products = []
        for product in self.products:
            if product.is_active():
                active_products.append(product)
        return active_products

    def order(self, shopping_list):
        """
        Processes an order consisting of products and quantities.

        Args:
            shopping_list (list): List of tuples (Product, quantity).

        Returns:
            float: Total price of all successfully purchased products.
        """
        total_price = 0
        for product, quantity in shopping_list:
            result = product.buy(quantity)
            if isinstance(result, str):
                print(f"Could not buy {product.name}: {result}")
            else:
                total_price += result
        return total_price

