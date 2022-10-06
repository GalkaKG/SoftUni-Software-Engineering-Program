symbols = ["-", ",", ".", "!", "?"]

with open('text.txt', 'r') as text_file:
    for idx, line in enumerate(text_file):
        if idx % 2 == 0:
            result = ' '.join(reversed(line.strip().split()))
            for symbol in symbols:
                result = result.replace(symbol, '@')
            print(result)
