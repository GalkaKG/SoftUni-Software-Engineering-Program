def numbers_searching(*args):
    duplicates = []
    for num in args:
        count_num = args.count(num)
        if count_num > 1 and num not in duplicates:
            duplicates.append(num)
    smallest_num = min(args)
    missing_num = []
    sorted_args = []
    for arg in args:
        if arg not in sorted_args:
            sorted_args.append(arg)
    for num in sorted(sorted_args):
        if num != smallest_num:
            missing_num = [smallest_num]
            smallest_num += 1
        smallest_num += 1

    return missing_num + [sorted(duplicates)]
