def list_manipulator(numbers, first_command, second_command, *args):
    if first_command == 'add' and second_command == 'beginning':
        args = list(args)
        args.extend(numbers)
        return args
    elif first_command == 'add' and second_command == 'end':
        numbers.extend(args)
        return numbers
    elif first_command == 'remove' and second_command == 'beginning':
        if args:
            num = args[0]
            for i in range(num):
                numbers.pop(0)
        else:
            numbers.pop(0)
        return numbers
    elif first_command == 'remove' and second_command == 'end':
        if args:
            num = args[0]
            for i in range(num):
                numbers.pop()
        else:
            numbers.pop()
        return numbers
