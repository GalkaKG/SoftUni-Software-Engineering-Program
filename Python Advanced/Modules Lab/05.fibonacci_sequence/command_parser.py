def parse_line(line):
    args = line.split()
    return ('Create', int(args[2])) if args[0] == 'Create' else ('Locate', int(args[1]))
