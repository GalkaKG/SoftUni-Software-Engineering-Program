def morse_code(text):
    words = ''
    result = ''
    is_end = False
    counter_len = 0
    for word in text:
        counter_len += 1
        if word != ' ' and word != '|':
            words += word
            if counter_len == len(text):
                result += list(MORSE_CODE_DICT.keys())[list(MORSE_CODE_DICT.values()).index(words)]
        if word == ' ':
            if not is_end and len(words) > 0:
                result += list(MORSE_CODE_DICT.keys())[list(MORSE_CODE_DICT.values()).index(words)]
                words = ''
            if is_end:
                is_end = False
        elif word == '|':
            words = ''
            is_end = True
            result += ' '
            continue

    return result


MORSE_CODE_DICT = {'A': '.-', 'B': '-...',
                   'C': '-.-.', 'D': '-..', 'E': '.',
                   'F': '..-.', 'G': '--.', 'H': '....',
                   'I': '..', 'J': '.---', 'K': '-.-',
                   'L': '.-..', 'M': '--', 'N': '-.',
                   'O': '---', 'P': '.--.', 'Q': '--.-',
                   'R': '.-.', 'S': '...', 'T': '-',
                   'U': '..-', 'V': '...-', 'W': '.--',
                   'X': '-..-', 'Y': '-.--', 'Z': '--..',
                   }
morse_code_text = input()
print(morse_code(morse_code_text))
