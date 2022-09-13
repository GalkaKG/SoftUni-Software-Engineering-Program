from collections import deque

price_bullet = int(input())
size_of_the_gun_barrel = int(input())
bullets = [int(x) for x in input().split()]
locks = deque([int(x) for x in input().split()])
value_of_intelligence = int(input())

bullets_counter = 0
gun_barrel_counter = size_of_the_gun_barrel

while True:
    if not bullets or not locks:
        break

    shot_bullet = bullets.pop()

    if gun_barrel_counter > 0:
        if shot_bullet <= locks[0]:
            print('Bang!')
            locks.popleft()
        else:
            print('Ping!')
        gun_barrel_counter -= 1
        bullets_counter += 1

    if gun_barrel_counter == 0 and bullets:
        print('Reloading!')
        gun_barrel_counter = size_of_the_gun_barrel

if locks:
    print(f"Couldn't get through. Locks left: {len(locks)}")
else:
    money = value_of_intelligence - (price_bullet * bullets_counter)
    print(f"{len(bullets)} bullets left. Earned ${money}")
