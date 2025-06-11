import products
import store

# Setup initial stock of inventory
product_list = [
    products.Product("MacBook Air M2", price=1450, quantity=100),
    products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
    products.Product("Google Pixel 7", price=500, quantity=250)
]
best_buy = store.Store(product_list)


def start():
    while True:
        print("\n--- Store Menu ---")
        print("1. List all products in store")
        print("2. Show total number of products")
        print("3. Make an order")
        print("4. Quit")
        try:
            user_selection = int(input("Please choose a number: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if user_selection == 1:
            print("\nAvailable Products:")
            for idx, product in enumerate(best_buy.get_all_products()):
                print(f"{idx + 1}. {product.show()}")

        elif user_selection == 2:
            print("Total unique products in store:", best_buy.get_total_quantity())

        elif user_selection == 3:
            shopping_list = get_user_input()
            total = best_buy.order(shopping_list)
            print(f"Thanks for buying from us! Total cost of your order: {total} dollars.")

        elif user_selection == 4:
            print("Bye bye!")
            break

        else:
            print("Invalid input. Please enter a number between 1 and 4.")


def get_user_input():
    shopping_list = []

    while True:
        print("\nCurrent Products:")
        all_products = best_buy.get_all_products()
        for idx, product in enumerate(all_products):
            print(f"{idx + 1}. {product.show()}")

        user_input = input("Enter product number (or press Enter to finish): ")
        if user_input == "":
            break

        try:
            product_index = int(user_input)
            selected_product = all_products[product_index]
        except (ValueError, IndexError):
            print("Invalid product number. Please try again.")
            continue

        amount_input = input(f"How many of '{selected_product.name}' would you like to order? ")
        try:
            amount = int(amount_input)
            if amount <= 0:
                print("Please enter a positive number.")
                continue
        except ValueError:
            print("Invalid quantity. Please enter a number.")
            continue

        shopping_list.append((selected_product, amount))

    return shopping_list



start()
