def genrange(start, end):
    i = start
    while i <= end:
        yield i
        i += 1


print(list(genrange(1, 10)))
