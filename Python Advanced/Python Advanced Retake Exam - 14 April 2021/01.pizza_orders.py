from collections import deque

pizzas = deque([int(x) for x in input().split(', ')])
employees = [int(x) for x in input().split(', ')]

total_pizzas = 0

while pizzas and employees:
    if 0 >= pizzas[0] or pizzas[0] > 10:
        pizzas.popleft()
        continue

    if pizzas[0] <= employees[-1]:
        total_pizzas += pizzas[0]
        pizzas.popleft()
        employees.pop()
    else:
        pizzas[0] -= employees[-1]
        total_pizzas += employees[-1]
        employees.pop()

if not pizzas:
    print(f'All orders are successfully completed!\nTotal pizzas made: {total_pizzas}')
    if employees:
        print(f'Employees: {", ".join([str(x) for x in employees])}')
else:
    print(f'Not all orders are completed.\nOrders left: {", ".join([str(x) for x in pizzas])}')
