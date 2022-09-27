def shopping_cart(*args):
    meals_dict = {'Soup': [], 'Pizza': [], 'Dessert': []}
    print_result = ''

    for meals in args:
        if meals == 'Stop':
            break
        type_of_meal, product = meals
        if type_of_meal == 'Soup' and len(meals_dict['Soup']) == 3:
            continue
        elif type_of_meal == 'Pizza' and len(meals_dict['Pizza']) == 4:
            continue
        elif type_of_meal == 'Dessert' and len(meals_dict['Dessert']) == 2:
            continue
        if product not in meals_dict[type_of_meal]:
            meals_dict[type_of_meal].append(product)

    for k, v in sorted(meals_dict.items(), key=lambda x: (-len(x[1]), x[0])):
        print_result += f'{k}:\n'
        for el in sorted(v):
            print_result += f' - {el}\n'

    if len(meals_dict['Soup']) == 0 and len(meals_dict['Pizza']) == 0 and len(meals_dict['Dessert']) == 0:
        return 'No products in the cart!'
    return print_result
