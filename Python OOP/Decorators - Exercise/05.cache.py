def cache(func_ref):
    log = {}

    def wrapper(num):
        if num in log:
            return log[num]
        result = func_ref(num)
        log[num] = result

        return result

    wrapper.log = log
    return wrapper


@cache
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


fibonacci(3)
print(fibonacci.log)

fibonacci(4)
print(fibonacci.log)
