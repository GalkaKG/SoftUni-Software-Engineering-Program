text = input()

symbols = {}
for ch in text:
    if ch in symbols:
        symbols[ch] += 1
    else:
        symbols[ch] = 1

for key, value in sorted(symbols.items()):
    print(f'{key}: {value} time/s')
