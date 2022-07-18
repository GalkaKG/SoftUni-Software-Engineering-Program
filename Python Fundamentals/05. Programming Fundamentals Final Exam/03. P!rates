cities_population = {}
cities_gold = {}

while True:
    command = input()
    if command == 'Sail':
        break

    command = command.split('||')
    city = command[0]
    population = int(command[1])
    gold = int(command[2])

    if city not in cities_population:
        cities_population[city] = population
    else:
        cities_population[city] += population

    if city not in cities_gold:
        cities_gold[city] = gold
    else:
        cities_gold[city] += gold

while True:
    command = input()
    if command == 'End':
        break
    command = command.split('=>')

    if 'Plunder' in command:
        town = command[1]
        people = int(command[2])
        gold = int(command[3])
        cities_population[town] -= people
        cities_gold[town] -= gold
        print(f'{town} plundered! {gold} gold stolen, {people} citizens killed.')

        if cities_population[town] == 0 or cities_gold[town] == 0:
            print(f"{town} has been wiped off the map!")
            del cities_population[town]
            del cities_gold[town]

    elif 'Prosper' in command:
        town = command[1]
        gold = int(command[2])

        if gold < 0:
            print("Gold added cannot be a negative number!")
        else:
            cities_gold[town] += gold
            print(f"{gold} gold added to the city treasury. {town} now has {cities_gold[town]} gold.")

if len(cities_population) > 0 and len(cities_gold) > 0:
    print(f'Ahoy, Captain! There are {len(cities_population)} wealthy settlements to go to:')
    for key, value in cities_population.items():
        print(f'{key} -> Population: {value} citizens, Gold: {cities_gold[key]} kg')
else:
    print("Ahoy, Captain! All targets have been plundered and destroyed!")
