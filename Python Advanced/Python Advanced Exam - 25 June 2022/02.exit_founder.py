from collections import deque

players = deque(input().split(', '))

matrix = [input().split() for _ in range(6)]
coordinates = eval(input())
ignored_players_dict = {}

while coordinates:
    row, col = coordinates
    player = players.popleft()

    if len(ignored_players_dict) > 0 and player in ignored_players_dict.keys():
        players.append(player)
        del ignored_players_dict[player]
        coordinates = eval(input())
        continue

    if matrix[row][col] == 'E':
        print(f"{player} found the Exit and wins the game!")
        break

    elif matrix[row][col] == 'T':
        print(f"{player} is out of the game! The winner is {''.join(players)}.")
        break

    elif matrix[row][col] == 'W':
        print(f"{player} hits a wall and needs to rest.")
        players.append(player)
        if player not in ignored_players_dict:
            ignored_players_dict[player] = 1
        else:
            ignored_players_dict[player] += 1

    elif matrix[row][col] == '.':
        players.append(player)
        coordinates = eval(input())
        continue

    coordinates = eval(input())
