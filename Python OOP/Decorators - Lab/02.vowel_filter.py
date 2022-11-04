def vowel_filter(function):
    def wrapper():
        elements = function()
        return [el for el in elements if el in 'aouei']
    return wrapper


@vowel_filter
def get_letters():
    return ["a", "b", "c", "d", "e"]


print(get_letters())
