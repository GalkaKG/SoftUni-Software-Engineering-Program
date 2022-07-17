from string import ascii_lowercase


def extract_func(text):
    current_num = [num for num in text if num.isdigit()]
    result = 0

    for i in range(len(text)):
        if text[i].isalpha():
            index = ascii_lowercase.index(text[i].lower()) + 1

            if i == 0:
                if text[i] == text[i].lower():
                    result = int(''.join(current_num)) * index
                else:
                    result = int(''.join(current_num)) / index
            else:
                if text[i] == text[i].lower():
                    result += index
                else:
                    result -= index

    return result


def letters_change_numbers(data):
    result = 0

    for num in data:
        result += extract_func(num)

    print(f'{result:.2f}')


data = input().split()
letters_change_numbers(data)
