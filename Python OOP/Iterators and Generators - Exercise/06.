def fibonacci():
    fib0, fib1 = 0, 1

    yield fib0
    yield fib1

    while True:
        next_num = fib0 + fib1
        yield next_num
        fib0 = fib1
        fib1 = next_num
