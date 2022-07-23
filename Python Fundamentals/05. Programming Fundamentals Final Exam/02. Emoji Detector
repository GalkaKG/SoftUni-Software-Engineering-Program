import re

text = input()

pattern = r'::[A-Z][a-z]{2,}::|\*{2}[A-Z][a-z]{2,}\*{2}'
threshold = re.findall(r"\d", text)
cool_threshold = 1
for num in threshold:
    cool_threshold *= int(num)

emojis = re.findall(pattern, text)
cool_emojis_list = []

for emoji in emojis:
    result = 0
    for ch in emoji:
        if ch.isalpha():
            result += ord(ch)
    if result >= cool_threshold:
        cool_emojis_list.append(emoji)

print(f'Cool threshold: {cool_threshold}')
print(f'{len(emojis)} emojis found in the text. The cool ones are:')
for emoji in cool_emojis_list:
    print(emoji)
