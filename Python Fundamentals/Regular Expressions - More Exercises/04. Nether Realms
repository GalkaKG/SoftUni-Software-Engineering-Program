import re

input_line = input()
demon_names = re.findall(r'[^,\s]+', input_line)
demons_dict = {}

for demon in range(len(demon_names)):
    health = 0
    pattern_health = r'[^0-9\+\-\*\/\.]'
    health_expression = re.findall(pattern_health, demon_names[demon])
    for ch in health_expression:
        health += ord(ch)

    damage = 0
    pattern_damage = r'(\-|\+)?\d+\.?\d*|\d'
    damage_expression = re.finditer(pattern_damage, demon_names[demon])
    for num in damage_expression:
        damage += float(num.group())
    if '*' in demon_names[demon]:
        for i in range(demon_names[demon].count('*')):
            damage *= 2
    if '/' in demon_names[demon]:
        for i in range(demon_names[demon].count('/')):
            damage /= 2
    demons_dict[demon_names[demon]] = [health, damage]

demons_dict = dict(sorted(demons_dict.items(), key=lambda x: x[0]))
for k, v in demons_dict.items():
    print(f'{k} - {v[0]} health, {v[1]:.2f} damage')
