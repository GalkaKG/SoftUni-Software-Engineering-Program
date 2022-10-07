from os import path, remove

while True:
    command = input()
    if command == 'End':
        break

    command = command.split('-')
    file_name = command[1]

    if 'Create' in command:
        open(file_name, 'w').close()
    elif 'Add' in command:
        content = command[2]
        with open(file_name, 'a') as file:
            file.write(content + '\n')
    elif 'Replace' in command:
        old_string, new_string = command[2], command[3]
        try:
            with open(file_name, 'r+') as file:
                new_content = file.read().replace(old_string, new_string)
                file.seek(0)
                file.truncate()
                file.write(new_content)
        except FileNotFoundError:
            print('An error occurred')
    elif 'Delete' in command:
        if path.exists(file_name):
            remove(file_name)
        else:
            print('An error occurred')
