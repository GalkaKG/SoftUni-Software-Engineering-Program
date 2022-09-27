def flights(*args):
    data = {}
    i, key = 0, ''
    for element in args:
        if element == 'Finish':
            break
        i += 1
        if i % 2 == 0:
            value = element
            if key not in data:
                data[key] = value
            else:
                data[key] += value
        else:
            key = element
    return data
