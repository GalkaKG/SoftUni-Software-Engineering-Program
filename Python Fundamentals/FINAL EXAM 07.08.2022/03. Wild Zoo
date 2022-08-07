animals_food = {}
animals_area = {}

while True:
    command = input()
    if command == 'EndDay':
        break
    command = command.split(': ')
    data = command[1].split('-')
    if 'Add' in command:
        animal_name = data[0]
        needed_food_quantity = int(data[1])
        area = data[2]
        if animal_name not in animals_food:
            animals_food[animal_name] = needed_food_quantity
        else:
            animals_food[animal_name] += needed_food_quantity
        if area not in animals_area:
            animals_area[area] = [animal_name]
        elif animal_name not in animals_area[area]:
            animals_area[area].append(animal_name)
    elif 'Feed' in command:
        animal_name = data[0]
        food = int(data[1])
        if animal_name in animals_food:
            animals_food[animal_name] -= food
            if animals_food[animal_name] <= 0:
                print(f'{animal_name} was successfully fed')
                del animals_food[animal_name]
                area = ''
                for k, v in animals_area.items():
                    if animal_name in v:
                        area = k
                animals_area[area].remove(animal_name)
                if len(animals_area[area]) == 0:
                    del animals_area[area]

print('Animals:')
for k, v in animals_food.items():
    print(f' {k} -> {v}g')
print('Areas with hungry animals:')
for k, v in animals_area.items():
    print(f' {"".join(k)}: {len(v)}')
