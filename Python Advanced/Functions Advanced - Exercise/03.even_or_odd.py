def even_odd(*args):
    filter_command = args[-1]
    parity = 0 if filter_command == 'even' else 1
    result = []
    for idx in range(len(args) - 1):
        number = args[idx]
        if number % 2 == parity:
            result.append(number)

    return result
