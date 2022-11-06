def type_check(type_):
    def decorator(func_ref):
        def wrapper(param):
            if not isinstance(param, type_):
                return 'Bad Type'
            return func_ref(param)

        return wrapper

    return decorator


@type_check(int)
def times2(num):
    return num * 2


print(times2(2))
print(times2('Not A Number'))


@type_check(str)
def first_letter(word):
    return word[0]


print(first_letter('Hello World'))
print(first_letter(['Not', 'A', 'String']))
