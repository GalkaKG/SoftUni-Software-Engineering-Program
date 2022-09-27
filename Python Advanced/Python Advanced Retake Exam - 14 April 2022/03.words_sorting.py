def words_sorting(*args):
    words_dict = {}

    for word in args:
        sum_chars = 0
        for ch in word:
            sum_chars += ord(ch)

        if word not in words_dict:
            words_dict[word] = sum_chars
        else:
            words_dict[word] += sum_chars

    is_odd = True if sum(words_dict.values()) % 2 != 0 else False

    if is_odd:
        sorted_words = sorted(words_dict.items(), key=lambda x: -x[1])
    else:
        sorted_words = sorted(words_dict.items(), key=lambda x: x[0])

    print_result = ''
    for k, v in sorted_words:
        print_result += f'{k} - {v}\n'

    return print_result
