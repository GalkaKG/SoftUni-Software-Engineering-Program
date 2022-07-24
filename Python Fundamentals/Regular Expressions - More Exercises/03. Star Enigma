import re

num = int(input())

pattern = r'@(?P<name>[A-Z][a-z]+)([^@\-!:>]*?):(?P<population>\d+)([^@\-!:>]*?)!(?P<attack>[A|D])!([^@\-!:>]*?)->(?P<soldier_count>\d+)'
attacked_planets = []
destroyed_planets = []

for i in range(num):
    message = input()
    count_letters = 0
    new_message = ''
    for ch in message:
        if ch.lower() in ['s', 't', 'a', 'r']:
            count_letters += 1
    for value in message:
        new_message += chr(ord(value) - count_letters)

    valids = re.finditer(pattern, new_message)
    for valid in valids:
        name = valid.group('name')
        attack = valid.group('attack')
        if attack == 'A':
            attacked_planets.append(name)
        elif attack == 'D':
            destroyed_planets.append(name)

attacked_planets.sort()
destroyed_planets.sort()
print(f'Attacked planets: {len(attacked_planets)}')
for attacked_planet in attacked_planets:
    print(f'-> {attacked_planet}')
print(f'Destroyed planets: {len(destroyed_planets)}')
for destroyed_planet in destroyed_planets:
    print(f'-> {destroyed_planet}')
