initial_array_value = input().split()
command = input()

while command != 'end':
    command = command.split()
    if 'swap' in command:
        index1 = int(command[1])
        index2 = int(command[2])
        number_on_index_1 = initial_array_value[index1]
        initial_array_value[index1] = initial_array_value[index2]
        initial_array_value[index2] = number_on_index_1
    elif 'multiply' in command:
        index1 = int(command[1])
        index2 = int(command[2])
        result = int(initial_array_value[index1]) * int(initial_array_value[index2])
        initial_array_value.pop(index1)
        initial_array_value.insert(index1, str(result))

    elif 'decrease' in command:
        for i in range(len(initial_array_value)):
            current_number = int(initial_array_value[i])
            current_number -= 1
            initial_array_value[i] = str(current_number)

    command = input()

print(', '.join(initial_array_value))
