from collections import deque

customers = deque([int(x) for x in input().split(', ')])
taxis = [int(x) for x in input().split(', ')]

total_time = 0

while customers and taxis:
    customer = customers.popleft()
    taxi_time = taxis.pop()

    if taxi_time >= customer:
        total_time += customer
    else:
        customers.appendleft(customer)

if not customers:
    print(f'All customers were driven to their destinations\nTotal time: {total_time} minutes')
else:
    print(f'Not all customers were driven to their destinations\nCustomers left: {", ".join([str(x) for x in customers])}')
