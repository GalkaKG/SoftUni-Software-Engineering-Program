from collections import deque

males = [int(x) for x in input().split() if int(x) > 0]
females = deque([int(x) for x in input().split() if int(x) > 0])

matches = 0

while males and females:
    if females[0] % 25 == 0:
        females.popleft()
        if females:
            females.popleft()
    elif males[-1] % 25 == 0:
        males.pop()
        if males:
            males.pop()
    elif females[0] == males[-1]:
        matches += 1
        males.pop()
        females.popleft()
    else:
        females.popleft()
        males[-1] -= 2
        if males[-1] <= 0:
            males.pop()

print(f"Matches: {matches}")
if males:
    print(f"Males left: {', '.join([str(x) for x in reversed(males)])}")
else:
    print("Males left: none")
if females:
    print(f"Females left: {', '.join([str(x) for x in females])}")
else:
    print("Females left: none")
