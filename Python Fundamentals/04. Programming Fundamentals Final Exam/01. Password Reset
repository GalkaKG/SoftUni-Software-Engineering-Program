text = input()

while True:
    command = input()
    if command == 'Done':
        break
    command = command.split()

    if 'TakeOdd' in command:
        text = ''.join([text[i] for i in range(len(text)) if i % 2 != 0])
        print(text)

    elif 'Cut' in command:
        index = int(command[1])
        length = int(command[2])
        text = text[:index] + text[index + length:]
        print(text)

    elif 'Substitute' in command:
        substring = command[1]
        substitute = command[2]
        if substring in text:
            text = text.replace(substring, substitute)
            print(text)
        else:
            print('Nothing to replace!')

print(f'Your password is: {text}')
