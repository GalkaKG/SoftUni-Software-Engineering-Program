def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def mul(a, b):
    return a * b


def div(a, b):
    return a / b


def pow(a, b):
    return a ** b


def calculate(a, b, op):
    if op == '+':
        return add(a, b)
    if op == '-':
        return sub(a, b)
    if op == '*':
        return mul(a, b)
    if op == '/':
        return div(a, b)
    if op == '^':
        return pow(a, b)
    raise ValueError('Not supported operation')
