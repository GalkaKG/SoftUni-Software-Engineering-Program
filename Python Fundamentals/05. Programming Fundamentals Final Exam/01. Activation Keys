def contains_func(activation_key, substr):
    if substr in activation_key:
        return f'{activation_key} contains {substr}'
    else:
        return 'Substring not found!'


def flip_func(activation_key, type_of_letters, start_idx, end_idx):
    if 'Upper' in type_of_letters:
        activation_key = activation_key[:start_idx] + activation_key[start_idx:end_idx].upper() + activation_key[end_idx:]
    elif 'Lower' in type_of_letters:
        activation_key = activation_key[:start_idx] + activation_key[start_idx:end_idx].lower() + activation_key[end_idx:]
    return activation_key


def slice_func(activation_key, start_idx, end_idx):
    substr = activation_key[start_idx:end_idx]
    activation_key = activation_key.replace(substr, '')
    return activation_key


text = input()

while True:
    command = input()
    if command == 'Generate':
        break
    command = command.split('>>>')

    if 'Contains' in command:
        substring = command[1]
        print(contains_func(text, substring))

    elif 'Flip' in command:
        upper_or_lower = command[1]
        start_index = int(command[2])
        end_index = int(command[3])
        text = flip_func(text, upper_or_lower, start_index, end_index)
        print(text)

    elif 'Slice' in command:
        start_index = int(command[1])
        end_index = int(command[2])
        text = slice_func(text, start_index, end_index)
        print(text)

print(f'Your activation key is: {text}')
