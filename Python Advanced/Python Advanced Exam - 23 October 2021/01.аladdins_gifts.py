from collections import deque

materials = [int(x) for x in input().split()]
magic_levels = deque([int(x) for x in input().split()])

gifts_type_dict = {
    'Gemstone': [100, 199],
    'Porcelain Sculpture': [200, 299],
    'Gold': [300, 399],
    'Diamond Jewellery': [400, 499]
}

dict_with_gifts = {}

while materials and magic_levels:
    sum_materials = materials[-1] + magic_levels[0]

    if sum_materials < 100:
        if sum_materials % 2 == 0:
            materials[-1] *= 2
            magic_levels[0] *= 3
            sum_materials = materials[-1] + magic_levels[0]
        else:
            sum_materials *= 2
    elif sum_materials > 499:
        sum_materials /= 2

    for k, v in gifts_type_dict.items():
        if v[0] <= sum_materials <= v[1]:
            if k in dict_with_gifts:
                dict_with_gifts[k] += 1
            else:
                dict_with_gifts[k] = 1
    materials.pop()
    magic_levels.popleft()

if 'Gemstone' in dict_with_gifts.keys() and 'Porcelain Sculpture' in dict_with_gifts.keys() \
        or 'Gold' in dict_with_gifts.keys() and 'Diamond Jewellery' in dict_with_gifts.keys():
    print("The wedding presents are made!")
else:
    print("Aladdin does not have enough wedding presents.")
if materials:
    print(f"Materials left: {', '.join([str(x) for x in materials])}")
if magic_levels:
    print(f"Magic left: {', '.join([str(x) for x in magic_levels])}")
for k, v in sorted(dict_with_gifts.items(), key=lambda x: x[0]):
    print(f'{k}: {v}')
