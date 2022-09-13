from collections import deque

cups = deque([int(x) for x in input().split()])
bottles = [int(x) for x in input().split()]

wasted_water = 0

while True:
    if not cups or not bottles:
        break
    else:
        current_cup = cups[0]
        current_bottle = bottles[-1]

    if current_bottle >= current_cup:
        wasted_water += (current_bottle - current_cup)
        bottles.pop()
        cups.popleft()
    elif current_cup > current_bottle:
        while current_cup > 0:
            if not bottles:
                break
            current_bottle = bottles[-1]
            last_cup = current_cup
            current_cup -= current_bottle
            current_bottle -= last_cup
            if current_bottle > 0:
                wasted_water += current_bottle
            bottles.pop()
            last_cup = 0
        cups.popleft()

if not cups:
    print(f"Bottles: {' '.join([str(x) for x in bottles])}")
else:
    print(f"Cups: {' '.join([str(x) for x in cups])}")

print(f"Wasted litters of water: {wasted_water}")
