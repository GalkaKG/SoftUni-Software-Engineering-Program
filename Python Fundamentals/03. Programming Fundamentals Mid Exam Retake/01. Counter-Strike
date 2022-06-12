energy = int(input())
command = input()
won_battles = 0

while command != 'End of battle':
    distance = int(command)

    if energy < distance:
        print(f'Not enough energy! Game ends with {won_battles} won battles and {energy} energy')
        break

    energy -= distance
    won_battles += 1

    if won_battles % 3 == 0:
        energy += won_battles

    command = input()

if command == 'End of battle':
    print(f'Won battles: {won_battles}. Energy left: {energy}')
