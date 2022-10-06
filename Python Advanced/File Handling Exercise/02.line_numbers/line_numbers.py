from string import punctuation

with open('text.txt', 'r') as text_file, open('output.txt', 'w') as output_file:
    for row, line in enumerate(text_file):
        letters_count = len([x for x in line if x.isalpha()])
        symbols_count = len([x for x in line if x in punctuation])
        output_file.write(f'Line {row + 1}: {line.strip()} ({letters_count})({symbols_count})\n')
