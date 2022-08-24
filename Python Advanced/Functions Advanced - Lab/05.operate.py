from functools import reduce


def operate(sign, *args):
    return reduce(lambda x, y: eval(f'{x} {sign} {y}'), args)


print(operate('+', 2, 2, 6))
