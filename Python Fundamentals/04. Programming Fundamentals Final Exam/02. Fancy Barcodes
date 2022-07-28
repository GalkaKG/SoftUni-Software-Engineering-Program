import re

n = int(input())

pattern = r'@#+[A-Z][a-z0-9A-Z]{4,}[A-Z]@#+'

for i in range(n):
    barcode = input()
    valid = re.findall(pattern, barcode)
    if valid:
        product_group = re.findall(r'\d+', str(valid))
        product_group = ''.join(product_group)
        if product_group:
            print(f'Product group: {product_group}')
        else:
            print('Product group: 00')
    else:
        print('Invalid barcode')
