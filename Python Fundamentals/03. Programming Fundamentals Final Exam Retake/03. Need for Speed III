# decision 1 without functions:

n = int(input())
car_mileage = {}
car_fuel = {}

for _ in range(n):
    command = input().split('|')
    car = command[0]
    mileage = int(command[1])
    fuel = int(command[2])
    car_mileage[car] = mileage
    car_fuel[car] = fuel

while True:
    command = input()
    if command == 'Stop':
        break
    command = command.split(' : ')
    car = command[1]

    if 'Drive' in command:
        distance = int(command[2])
        fuel = int(command[3])
        if car_fuel[car] < fuel:
            print('Not enough fuel to make that ride')
        elif car_fuel[car] >= fuel:
            car_mileage[car] += distance
            car_fuel[car] -= fuel
            print(f'{car} driven for {distance} kilometers. {fuel} liters of fuel consumed.')
        if car_mileage[car] >= 100000:
            del car_mileage[car]
            print(f'Time to sell the {car}!')

    elif 'Refuel' in command:
        fuel = int(command[2])
        fuel_filled = 0
        if car_fuel[car] < 75:
            diff = 75 - car_fuel[car]
            if diff < fuel:
                fuel_filled = diff
                car_fuel[car] += fuel_filled
            else:
                fuel_filled = fuel
                car_fuel[car] += fuel_filled
        elif car_fuel[car] >= 75:
            fuel_filled = 0
        if car_fuel[car] >= 75:
            car_fuel[car] = 75
        print(f'{car} refueled with {fuel_filled} liters')

    elif 'Revert' in command:
        kilometers = int(command[2])
        car_mileage[car] -= kilometers
        if car_mileage[car] < 10000:
            car_mileage[car] = 10000
            continue
        print(f'{car} mileage decreased by {kilometers} kilometers')

for k, v in car_mileage.items():
    print(f'{k} -> Mileage: {v} kms, Fuel in the tank: {car_fuel[k]} lt.')
    
    
    
    
    
    
# decision 2 with functions:

def drive_func(kms, fl, car_ml, car_fl):
    if car_fl[car] < fl:
        print('Not enough fuel to make that ride')
    elif car_fl[car] >= fl:
        car_ml[car] += kms
        car_fl[car] -= fl
        print(f'{car} driven for {kms} kilometers. {fl} liters of fuel consumed.')
    if car_ml[car] >= 100000:
        del car_ml[car]
        print(f'Time to sell the {car}!')


def refuel_func(fl, car_fl):
    fuel_filled = 0
    if car_fl[car] < 75:
        diff = 75 - car_fl[car]
        if diff < fl:
            fuel_filled = diff
            car_fl[car] += fuel_filled
        else:
            fuel_filled = fl
            car_fl[car] += fuel_filled
    elif car_fl[car] >= 75:
        fuel_filled = 0
    if car_fl[car] >= 75:
        car_fl[car] = 75
    print(f'{car} refueled with {fuel_filled} liters')


def revert_func(kms, car_ml):
    car_ml[car] -= kms
    if car_ml[car] < 10000:
        car_ml[car] = 10000
        return
    print(f'{car} mileage decreased by {kms} kilometers')


n = int(input())
car_mileage = {}
car_fuel = {}

for _ in range(n):
    command = input().split('|')
    car = command[0]
    mileage = int(command[1])
    fuel = int(command[2])
    car_mileage[car] = mileage
    car_fuel[car] = fuel

while True:
    command = input()
    if command == 'Stop':
        break
    command = command.split(' : ')
    car = command[1]

    if 'Drive' in command:
        distance = int(command[2])
        fuel = int(command[3])
        drive_func(distance, fuel, car_mileage, car_fuel)

    elif 'Refuel' in command:
        fuel = int(command[2])
        refuel_func(fuel, car_fuel)

    elif 'Revert' in command:
        kilometers = int(command[2])
        revert_func(kilometers, car_mileage)

for k, v in car_mileage.items():
    print(f'{k} -> Mileage: {v} kms, Fuel in the tank: {car_fuel[k]} lt.')
    
