from itertools import permutations


def possible_permutations(elements):
    result = permutations(elements)
    for num in result:
        yield list(num)
