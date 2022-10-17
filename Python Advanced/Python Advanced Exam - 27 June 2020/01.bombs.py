# 1-st decision:

from collections import deque

bomb_effects = deque([int(x) for x in input().split(', ')])
bomb_casings = [int(x) for x in input().split(', ')]

materials = {
    40: 'Datura Bombs',
    60: 'Cherry Bombs',
    120: 'Smoke Decoy Bombs'
}

created_bombs = {
    'Datura Bombs': 0,
    'Cherry Bombs': 0,
    'Smoke Decoy Bombs': 0
}

is_bomb_pouch = False

while bomb_effects and bomb_casings and not is_bomb_pouch:
    bomb_effect = bomb_effects.popleft()
    bomb_casing = bomb_casings.pop()

    sum_of_both = bomb_effect + bomb_casing

    for k, v in materials.items():
        if sum_of_both == k:
            created_bombs[v] += 1
            break
    if sum_of_both not in materials.keys():
        bomb_casing -= 5
        bomb_casings.append(bomb_casing)
        bomb_effects.appendleft(bomb_effect)

    if created_bombs['Datura Bombs'] >= 3 and created_bombs['Cherry Bombs'] >= 3 and created_bombs['Smoke Decoy Bombs'] >= 3:
        is_bomb_pouch = True

if is_bomb_pouch:
    print("Bene! You have successfully filled the bomb pouch!")
else:
    print("You don't have enough materials to fill the bomb pouch.")

if bomb_effects:
    print(f"Bomb Effects: {', '.join([str(x) for x in bomb_effects])}")
else:
    print("Bomb Effects: empty")

if bomb_casings:
    print(f"Bomb Casings: {', '.join([str(x) for x in bomb_casings])}")
else:
    print("Bomb Casings: empty")

for k, v in sorted(created_bombs.items(), key=lambda x: x[0]):
    print(f'{k}: {v}')
    
    
    
# 2-nd decision:

from collections import deque

bombs_effects = deque([int(x) for x in input().split(', ')])
bombs_casing = [int(x) for x in input().split(', ')]
full_set = False

bombs = {
    'Cherry Bombs': 0,
    'Datura Bombs': 0,
    'Smoke Decoy Bombs': 0
}

while not full_set and bombs_effects and bombs_casing:
    effect = bombs_effects.popleft()
    casing = bombs_casing.pop()
    mix_effect = effect + casing

    for bomb, quantity in (("Datura Bombs", 40), ("Cherry Bombs", 60), ('Smoke Decoy Bombs', 120)):
        if mix_effect == quantity:
            bombs[bomb] += 1
            break
    else:
        bombs_casing.append(casing - 5)
        bombs_effects.appendleft(effect)
        continue

    if all(x >= 3 for x in bombs.values()):
        full_set = True

if full_set:
    set_result = "Bene! You have successfully filled the bomb pouch!"
else:
    set_result = "You don't have enough materials to fill the bomb pouch."

print(set_result)

if bombs_effects:
    bomb = f'Bomb Effects: {", ".join(str(x) for x in bombs_effects)}'
else:
    bomb = 'Bomb Effects: empty'

print(bomb)

if bombs_casing:
    casing_bomb = f'Bomb Casings: {", ".join(str(x) for x in bombs_casing)}'
else:
    casing_bomb = 'Bomb Casings: empty'

print(casing_bomb)

for bomb, quantity in bombs.items():
    print(f'{bomb}: {quantity}')
