targets_list = [int(number) for number in input().split()]
command = input()

while command != 'End':
    command = command.split()

    if 'Shoot' in command:
        index = int(command[1])
        power = int(command[2])
        if 0 <= index < len(targets_list):
            for i, string in enumerate(targets_list):
                if i == index:
                    string = int(string)
                    string -= power
                    targets_list[index] = string
            if targets_list[index] <= 0:
                targets_list.pop(index)

    elif 'Add' in command:
        index = int(command[1])
        value = int(command[2])
        if 0 <= index < len(targets_list):
            targets_list.insert(index, value)
        else:
            print("Invalid placement!")

    elif 'Strike' in command:
        index = int(command[1])
        radius = int(command[2])
        index_before = index - radius
        index_after = index + radius
        if 0 <= index_before < len(targets_list) and 0 <= index < len(targets_list) and 0 <= index_after < len(
                targets_list):
            targets_list = targets_list[:index_before] + targets_list[index_after+1:]
        else:
            print("Strike missed!" )

    command = input()

targets_list = list(map(str, targets_list))
print('|'.join(targets_list))
