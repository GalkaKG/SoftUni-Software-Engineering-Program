import re

number = int(input())
pattern = r'!([A-Z][a-z]{3,})!:\[([A-Za-z]{8,})\]'

for i in range(number):
    text = input()
    valid = re.match(pattern, text)
    if not valid:
        print('The message is invalid')
    if valid:
        expression = re.finditer(pattern, text)
        string_values = []
        command = ''
        for match in expression:
            command = match.group(1)
            string = match.group(2)
            for ch in string:
                string_values.append(str(ord(ch)))
        print(f'{command}: {" ".join(string_values)}')
