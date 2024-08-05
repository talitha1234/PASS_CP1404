def main():
    """Get product and quantity."""
    product_price_1 = float(input("Enter product 1 price: "))
    product_quantity_1 = int(input("Enter quantity of first product: "))
    product_price_2 = float(input("Enter product 2 price: "))
    product_quantity_2 = int(input("Enter quantity of second product: "))


def print_product(price_1, quantity_1, price_2, quantity_2):
    """Print the cheaper product."""
    if price_1 * quantity_1 > price_2 * quantity_2:
        print("Second product is cheaper.")
    elif price_1 * quantity_1 < price_2 * quantity_2:
        print("First product is cheaper.")
    else:
        print("Cost is the same.")


main()
