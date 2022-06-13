days_of_plunder = int(input())
daily_plunder = int(input())
expected_plunder = int(input())
plunder = 0

for day in range(1, days_of_plunder + 1):
    plunder += daily_plunder

    if day % 3 == 0:
        plunder += (daily_plunder * 0.50)

    if day % 5 == 0:
        plunder -= (plunder * 0.30)

if plunder >= expected_plunder:
    print(f'Ahoy! {plunder:.2f} plunder gained.')
else:
    print(f'Collected only {(plunder/expected_plunder * 100):.2f}% of the plunder.')
