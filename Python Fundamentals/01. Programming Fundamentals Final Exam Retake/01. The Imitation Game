# Decision 1 with functions:
def move(msg, num):
    msg = list(msg)
    msg[num:], msg[:num] = msg[:num], msg[num:]
    msg = ''.join(msg)
    return msg


def insert_func(msg, idx, val):
    msg = list(msg)
    msg.insert(idx, val)
    msg = ''.join(msg)
    return msg


def change_all(msg, substr, repl):
    msg = msg.replace(substr, repl)
    return msg


message = input()
while True:
    command = input()

    if command == 'Decode':
        break

    command = command.split('|')

    if 'Move' in command:
        number_of_letters = int(command[1])
        message = move(message, number_of_letters)

    if 'Insert' in command:
        index = int(command[1])
        value = command[2]
        message = insert_func(message, index, value)

    if 'ChangeAll' in command:
        substring = command[1]
        replacement = command[2]
        message = change_all(message, substring, replacement)

print(f'The decrypted message is: {message}')




# Decision 2 with no functions:
message = input()

while True:
    command = input()

    if command == 'Decode':
        break

    command = command.split('|')

    if 'Move' in command:
        number_of_letters = int(command[1])
        message = list(message)
        message[number_of_letters:], message[:number_of_letters] = message[:number_of_letters], message[number_of_letters:]
        message = ''.join(message)

    if 'Insert' in command:
        message = list(message)
        index = int(command[1])
        value = command[2]
        message.insert(index, value)
        message = ''.join(message)

    if 'ChangeAll' in command:
        substring = command[1]
        replacement = command[2]
        message = message.replace(substring, replacement)

print(f'The decrypted message is: {message}')
