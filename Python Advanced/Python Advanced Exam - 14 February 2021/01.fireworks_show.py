from collections import deque


def remove_elements(fireworks, explosive_power):
    fireworks.popleft()
    explosive_power.pop()


fireworks = deque([int(x) for x in input().split(', ') if int(x) > 0])
explosive_power = [int(x) for x in input().split(', ') if int(x) > 0]

fireworks_dict = {'Palm Fireworks': 0, 'Willow Fireworks': 0, 'Crossette Fireworks': 0}
perfect_show = False

while fireworks and explosive_power:
    sum_values = fireworks[0] + explosive_power[-1]

    if sum_values % 3 == 0 and sum_values % 5 != 0:
        fireworks_dict['Palm Fireworks'] += 1
        remove_elements(fireworks, explosive_power)
    elif sum_values % 5 == 0 and sum_values % 3 != 0:
        fireworks_dict['Willow Fireworks'] += 1
        remove_elements(fireworks, explosive_power)
    elif sum_values % 3 == 0 and sum_values % 5 == 0:
        fireworks_dict['Crossette Fireworks'] += 1
        remove_elements(fireworks, explosive_power)
    else:
        fireworks[0] -= 1
        if fireworks[0] <= 0:
            fireworks.popleft()
        else:
            fireworks.rotate(-1)

    if fireworks_dict['Palm Fireworks'] >= 3 and fireworks_dict['Willow Fireworks'] >= 3 \
            and fireworks_dict['Crossette Fireworks'] >= 3:
        perfect_show = True
        break

if perfect_show:
    print("Congrats! You made the perfect firework show!")
else:
    print("Sorry. You can't make the perfect firework show.")
if fireworks:
    print(f"Firework Effects left: {', '.join([str(x) for x in fireworks])}")
if explosive_power:
    print(f"Explosive Power left: {', '.join([str(x) for x in explosive_power])}")
for k, v in fireworks_dict.items():
    print(f"{k}: {v}")
