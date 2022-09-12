from collections import deque


def convert_str_to_seconds(str_time):
    hours, minutes, seconds = [int(x) for x in str_time.split(':')]
    return hours * 60 * 60 + minutes * 60 + seconds


def converts_seconds_to_str_time(seconds):
    seconds %= 24 * 60 * 60
    
    hours = seconds // (60 * 60)
    seconds %= (60 * 60)
    minutes = seconds // 60
    seconds %= 60
    return f'{hours:02d}:{minutes:02d}:{seconds:02d}'


robots_data = input().split(';')
process_time_by_robot = {}
busy_until_by_robot = {}

for robot_data in robots_data:
    name, process_time = robot_data.split('-')
    process_time_by_robot[name] = int(process_time)
    busy_until_by_robot[name] = -1

time = convert_str_to_seconds(input())
items = deque()

while True:
    line = input()
    if line == 'End':
        break
    items.append(line)

while items:
    time += 1
    item = items.popleft()

    for name, busy_until in busy_until_by_robot.items():
        if time >= busy_until:
            busy_until_by_robot[name] = time + process_time_by_robot[name]
            print(f'{name} - {item} [{converts_seconds_to_str_time(time)}]')
            break
    else:
        items.append(item)
