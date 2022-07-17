def find(text_result):
    type_treasure = ''
    coordinates = ''
    counter = 0
    for index, symbol in enumerate(text_result):
        if symbol == '&':
            counter += 1
            if counter == 1:
                index_start_type = index + 1
            if counter == 2:
                index_end_type = index
                type_treasure = text_result[index_start_type:index_end_type]
        if symbol == '<':
            index_coordinates_start = index + 1
        elif symbol == '>':
            index_coordinates_end = index
            coordinates = text_result[index_coordinates_start:index_coordinates_end]

    print(f'Found {type_treasure} at {coordinates}')


def treasure_finder(key_nums):
    while True:
        text = input()
        if text == 'find':
            break

        ord_value = 0
        text_result = ''

        i = 0
        while i < len(text):
            if i == len(key_nums):
                text = text[i:]
                i = 0
            ord_value = ord(text[i]) - int(key_nums[i])
            text_result += chr(ord_value)
            i += 1
        find(text_result)


key = input().split()
treasure_finder(key)
