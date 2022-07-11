destinations = input()
while True:
    command = input()

    if command == 'Travel':
        break

    command = command.split(':')
    if 'Add Stop' in command:
        index = int(command[1])
        string = command[2]
        destinations = list(destinations)
        if -1 < index < len(destinations):
            destinations.insert(index, string)
        destinations = ''.join(destinations)
        print(destinations)

    elif 'Remove Stop' in command:
        start_index = int(command[1])
        end_index = int(command[2])
        if -1 < start_index < len(destinations) and -1 < end_index < len(destinations):
            destinations = destinations[:start_index] + destinations[end_index + 1:]
        print(destinations)

    elif 'Switch' in command:
        old_string = command[1]
        new_string = command[2]
        destinations = destinations.replace(old_string, new_string)
        print(destinations)

print(f'Ready for world tour! Planned stops: {destinations}')
