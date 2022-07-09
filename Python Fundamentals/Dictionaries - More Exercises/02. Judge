data = {}
students_points = {}

while True:
    command = input()

    if command == 'no more time':
        break

    username, contest, points = command.split(' -> ')
    points = int(points)

    if contest not in data:
        data[contest] = {}

    if username not in data[contest]:
        data[contest][username] = points

        if username not in students_points:
            students_points[username] = points
        else:
            students_points[username] += points
    else:
        if data[contest][username] < points:
            data[contest][username] = points
            students_points[username] = points

for k, v in data.items():
    number = 1
    print(f'{k}: {len(v)} participants')
    sorted_data = dict(sorted(v.items(), key=lambda x: (-x[1], x[0])))
    for k2, v2 in sorted_data.items():
        print(f'{number}. {k2} <::> {v2}')
        number += 1
print('Individual standings:')
sorted_students_points = sorted(students_points.items(), key=lambda kvpt: (-kvpt[1], kvpt[0]))
number = 1
for name, points in sorted_students_points:
    print(f'{number}. {name} -> {points}')
    number += 1
