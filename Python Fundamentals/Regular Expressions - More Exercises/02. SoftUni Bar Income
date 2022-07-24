import re

pattern = r"%(?P<name>[A-Z][a-z]+)%([^|$%.]*?)<(?P<product>\w+)>([^|$%.]*?)\|(?P<count>\d*)\|([^|$%.]*?)(?P<price>\d*\.?\d{0,2}?)\$"
total_sum = 0

while True:
    line = input()
    if line == 'end of shift':
        break

    valids = re.finditer(pattern, line)
    for valid in valids:
        name = valid.group('name')
        product = valid.group('product')
        count = valid.group('count')
        price = valid.group('price')
        sum_price = int(count) * float(price)
        total_sum += sum_price

        print(f'{name}: {product} - {sum_price:.2f}')

print(f'Total income: {total_sum:.2f}')
