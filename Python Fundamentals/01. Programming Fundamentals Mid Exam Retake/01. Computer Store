command = input()
total_sum = 0
condition = False

while command != 'special':
    if command == 'regular':
        break
    numbers = float(command)

    if numbers < 0:
        print('Invalid price!')
        command = input()
        continue

    total_sum += numbers

    if total_sum == 0:
        print('Invalid order!')

    command = input()

total_amount_of_taxes = total_sum * 0.20
total_sum_with_taxes = total_sum + total_amount_of_taxes

if command == 'special':
    total_sum_with_taxes -= (total_sum_with_taxes * 0.10)

if total_sum_with_taxes == 0:
    print('Invalid order!')
else:
    print(f"Congratulations you've just bought a new computer!\nPrice without taxes: {total_sum:.2f}$\nTaxes:"
          f" {total_amount_of_taxes:.2f}$\n-----------\nTotal price: {total_sum_with_taxes:.2f}$")
