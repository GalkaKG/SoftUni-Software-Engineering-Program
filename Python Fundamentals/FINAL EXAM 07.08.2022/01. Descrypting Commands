text = input()

while True:
    command = input()
    if command == 'Finish':
        break
    command = command.split()
    if 'Replace' in command:
        current_char = command[1]
        new_char = command[2]
        text = str(text).replace(current_char, new_char)
        print(text)
    elif 'Cut' in command:
        start_index = int(command[1])
        end_index = int(command[2])
        if 0 <= start_index < len(text) and 0 <= end_index < len(text):
            substring = text[start_index:end_index+1]
            text = str(text).replace(substring, '')
            print(text)
        else:
            print('Invalid indices!')
    elif 'Make' in command:
        if 'Upper' in command[1]:
            text = text.upper()
            print(text)
        elif 'Lower' in command[1]:
            text = text.lower()
            print(text)
    elif 'Check' in command:
        string = command[1]
        if string in text:
            print(f'Message contains {string}')
        else:
            print(f"Message doesn't contain {string}")
    elif 'Sum' in command:
        start_index = int(command[1])
        end_index = int(command[2])
        if 0 <= start_index < len(text) and 0 <= end_index < len(text):
            substring = text[start_index:end_index + 1]
            result = 0
            for ch in substring:
                result += ord(ch)
            print(result)
        else:
            print('Invalid indices!')
