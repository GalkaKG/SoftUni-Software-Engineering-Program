pirate_ship = list(map(int, input().split('>')))
warship_status = list(map(int, input().split('>')))
maximum_health = int(input())
break_condition = False

while True:
    command = input()

    if break_condition:
        break

    if command == 'Retire':
        break

    command = command.split()

    if 'Fire' in command:
        index = int(command[1])
        damage = int(command[2])
        if -1 < index < len(warship_status):
            warship_status[index] = warship_status[index] - damage
            if warship_status[index] <= 0:
                print("You won! The enemy ship has sunken.")
                break_condition = True
                break

    elif 'Defend' in command:
        start_index = int(command[1])
        end_index = int(command[2])
        damage = int(command[3])
        if -1 < start_index < len(pirate_ship) and -1 < end_index < len(pirate_ship):
            for i in pirate_ship:
                pirate_ship[start_index] = pirate_ship[start_index] - damage
                if pirate_ship[start_index] <= 0:
                    print("You lost! The pirate ship has sunken.")
                    break_condition = True
                    break
                if start_index == end_index:
                    break
                start_index += 1

    elif 'Repair' in command:
        index = int(command[1])
        health = int(command[2])
        if -1 < index < len(pirate_ship):
            pirate_ship[index] = pirate_ship[index] + health
            if pirate_ship[index] > maximum_health:
                pirate_ship[index] = maximum_health

    elif 'Status' in command:
        percent = maximum_health * 0.20
        count_for_repair = len([x for x in pirate_ship if x < percent])
        print(f'{count_for_repair} sections need repair.')

if not break_condition:
    print(f"Pirate ship status: {sum(pirate_ship)}")
    print(f"Warship status: {sum(warship_status)}")
