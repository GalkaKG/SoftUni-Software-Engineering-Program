def sorting_cheeses(**kwargs):
    sorted_cheeses = sorted(kwargs.items(), key=lambda kvpt: (-len(kvpt[1]), kvpt[0]))
    result = ''
    for name, quantities in sorted_cheeses:
        result += name + '\n'
        sorted_quantities = sorted(quantities, reverse=True)
        result += '\n'.join([str(el) for el in sorted_quantities]) + '\n'
    return result
