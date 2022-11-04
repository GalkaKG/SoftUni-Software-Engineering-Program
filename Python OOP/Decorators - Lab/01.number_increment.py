def number_increment(numbers):
    def increase():
        res = [x + 1 for x in numbers]
        return res

    return increase()


print(number_increment([1, 2, 3]))
