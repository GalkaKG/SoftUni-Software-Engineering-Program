from math import floor

money_in_lv = float(input())
money = floor(money_in_lv * 100)
coins_counter = 0

while money > 0:
    if money >= 200:
        money -= 200
        coins_counter += 1
    elif money >= 100:
        money -= 100
        coins_counter += 1
    elif money >= 50:
        money -= 50
        coins_counter += 1
    elif money >= 20:
        money -= 20
        coins_counter += 1
    elif money >= 10:
        money -= 10
        coins_counter += 1
    elif money >= 5:
        money -= 5
        coins_counter += 1
    elif money >= 2:
        money -= 2
        coins_counter += 1
    else:
        money -= 1
        coins_counter += 1

print(coins_counter)
