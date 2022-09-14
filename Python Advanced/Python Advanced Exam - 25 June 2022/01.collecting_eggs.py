from collections import deque

eggs = deque([int(x) for x in input().split(', ')])
pieces_of_paper = [int(x) for x in input().split(', ')]

filled_boxes = 0

while eggs and pieces_of_paper:
    if eggs[0] <= 0:
        eggs.popleft()
        continue

    if eggs[0] == 13:
        eggs.popleft()
        pieces_of_paper[0], pieces_of_paper[-1] = pieces_of_paper[-1], pieces_of_paper[0]
        continue

    if eggs[0] + pieces_of_paper[-1] <= 50:
        filled_boxes += 1
    eggs.popleft()
    pieces_of_paper.pop()

if filled_boxes > 0:
    print(f"Great! You filled {filled_boxes} boxes.")
else:
    print("Sorry! You couldn't fill any boxes!")
if eggs:    
    print(f'Eggs left: {", ".join([str(x) for x in eggs])}')
if pieces_of_paper:
    print(f'Pieces of paper left: {", ".join([str(x) for x in pieces_of_paper])}')
