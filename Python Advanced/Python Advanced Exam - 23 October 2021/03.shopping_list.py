def shopping_list(budget, **kwargs):
    bought_products = {}
    print_result = ''
    if budget < 100:
        return "You do not have enough budget."
    else:
        for product_name, value in kwargs.items():
            price, quantity = value[0], value[1]
            if len(bought_products) == 5:
                break
            calculate_price = price * quantity
            if calculate_price < budget:
                bought_products[product_name] = calculate_price
                budget -= calculate_price
        for product, total_price in bought_products.items():
            print_result += f"You bought {product} for {total_price:.2f} leva.\n"
        return print_result
