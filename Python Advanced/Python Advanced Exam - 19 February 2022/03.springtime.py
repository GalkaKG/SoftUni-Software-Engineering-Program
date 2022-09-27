# First decision:

def start_spring(**kwargs):
    collection_dict, print_result = {}, ''
    for value, key in kwargs.items():
        collection_dict[key] = collection_dict.get(key, []) + [value]
    for k, v in sorted(collection_dict.items(), key=lambda x: (-len(x[1]), x[0])):
        print_result += f'{k}:\n'
        for el in sorted(v):
            print_result += f'-{el}\n'
            
    return print_result



# Second decision:

def start_spring(**kwargs):
    collection_dict, print_result = {}, ''
    for value, key in kwargs.items():
        if key not in collection_dict:
            collection_dict[key] = []
        collection_dict[key].append(value)
    for k, v in sorted(collection_dict.items(), key=lambda x: (-len(x[1]), x[0])):
        print_result += f'{k}:\n'
        for el in sorted(v):
            print_result += f'-{el}\n'
    return print_result
