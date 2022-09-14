from collections import deque

bowls_of_ramen = [int(x) for x in input().split(', ')]
customers = deque([int(x) for x in input().split(', ')])

while bowls_of_ramen and customers:
    if bowls_of_ramen[-1] == customers[0]:
        bowls_of_ramen.pop()
        customers.popleft()
    elif bowls_of_ramen[-1] > customers[0]:
        bowls_of_ramen[-1] -= customers[0]
        customers.popleft()
    else:
        customers[0] -= bowls_of_ramen[-1]
        bowls_of_ramen.pop()

if not customers:
    print("Great job! You served all the customers.")
    if bowls_of_ramen:
        print(f"Bowls of ramen left: {', '.join([str(x) for x in bowls_of_ramen])}")
else:
    print("Out of ramen! You didn't manage to serve all customers.")
    print(f"Customers left: {', '.join([str(x) for x in customers])}")
