dungeon_rooms = input().split('|')
health = 100
bitcoins = 0
counter_rooms = 0
is_over = False

for i in range(len(dungeon_rooms)):
    rooms = dungeon_rooms[i]
    rooms = rooms.split()
    command = rooms[0]
    number = int(rooms[1])
    counter_rooms += 1

    if command == 'potion':
        current_health = health
        health += number
        if health > 100:
            health = 100
        print(f'You healed for {abs(health - current_health)} hp.')
        print(f'Current health: {health} hp.')
    elif command == 'chest':
        bitcoins += number
        print(f'You found {number} bitcoins.')
    else:
        health -= number
        if health > 0:
            print(f'You slayed {command}.')
        else:
            print(f'You died! Killed by {command}.')
            print(f'Best room: {counter_rooms}')
            is_over = True
            break

if not is_over:
    print("You've made it!")
    print(f"Bitcoins: {bitcoins}")
    print(f"Health: {health}")
