from fibonacci import create, locate
from command_parser import parse_line

nums = []
while True:
    line = input()
    if line == 'Stop':
        break
    command, arg = parse_line(line)
    if command == 'Create':
        nums = create(arg)
        print(*nums, sep=' ')
    else:
        idx = locate(arg, nums)
        output = f'The number {arg} is not in the sequence.' if idx == - 1 else f'The number - {arg} is at index {idx}'
        print(output)
