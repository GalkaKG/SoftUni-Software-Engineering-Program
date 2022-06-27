string_with_vehicles = input().split('>>')
initial_tax = 0
total_sum_tax = 0
total_taxes_collected = 0

for vehicles in string_with_vehicles:
    vehicles_number = vehicles.split()
    years_tax_should_paid = int(vehicles_number[1])
    kilometers = int(vehicles_number[2])

    if vehicles_number[0] == 'family':
        initial_tax = 50
        how_many_times_increase = kilometers // 3000
        total_sum_tax = initial_tax + (how_many_times_increase * 12) - (years_tax_should_paid * 5)

    elif vehicles_number[0] == 'heavyDuty':
        initial_tax = 80
        how_many_times_increase = kilometers // 9000
        total_sum_tax = initial_tax + (how_many_times_increase * 14) - (years_tax_should_paid * 8)
    elif vehicles_number[0] == 'sports':
        initial_tax = 100
        how_many_times_increase = kilometers // 2000
        total_sum_tax = initial_tax + (how_many_times_increase * 18) - (years_tax_should_paid * 9)
    else:
        print("Invalid car type.")
        continue

    total_taxes_collected += total_sum_tax

    print(f"A {vehicles_number[0]} car will pay {total_sum_tax:.2f} euros in taxes.")

print(f"The National Revenue Agency will collect {total_taxes_collected:.2f} euros in taxes.")
