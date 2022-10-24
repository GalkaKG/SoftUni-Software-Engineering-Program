from collections import deque

coffeine = [int(x) for x in input().split(', ')]
energy_drinks = deque([int(x) for x in input().split(', ')])

total_coffeine = 0
limit_per_day = 300

while coffeine and energy_drinks:
    last_milligrams_of_coffeine = coffeine.pop()
    first_drink = energy_drinks.popleft()

    result_of_both = last_milligrams_of_coffeine * first_drink

    if result_of_both + total_coffeine <= limit_per_day:
        total_coffeine += result_of_both
    else:
        energy_drinks.append(first_drink)
        if total_coffeine >= 30:
            total_coffeine -= 30
        elif 0 < total_coffeine < 30:
            total_coffeine -= total_coffeine

if energy_drinks:
    print(f"Drinks left: {', '.join([str(x) for x in energy_drinks])}")
else:
    print(f"At least Stamat wasn't exceeding the maximum caffeine.")

if total_coffeine >= 0:
    print(f"Stamat is going to sleep with {total_coffeine} mg caffeine.")
else:
    print(f"Stamat is going to sleep with 0 mg caffeine.")
