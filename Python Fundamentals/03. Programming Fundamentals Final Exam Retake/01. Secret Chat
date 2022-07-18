import re

secret_message = input()

while True:
    command = input()
    if command == 'Reveal':
        break
    command = command.split(':|:')

    if 'InsertSpace' in command:
        index = int(command[1])
        secret_message = list(secret_message)
        secret_message.insert(index, ' ')
        secret_message = ''.join(secret_message)
        print(secret_message)

    elif 'Reverse' in command:
        substring = command[1]
        if substring in secret_message:
            match = (re.search(substring, secret_message))
            start_index = match.start()
            end_index = match.end()
            secret_message = secret_message[:start_index] + secret_message[end_index:]
            secret_message += (substring[::-1])
            print(secret_message)
        else:
            print('error')

    elif 'ChangeAll' in command:
        substring = command[1]
        replacement = command[2]
        secret_message = secret_message.replace(substring, replacement)
        print(secret_message)

print(f'You have a new text message: {secret_message}')
