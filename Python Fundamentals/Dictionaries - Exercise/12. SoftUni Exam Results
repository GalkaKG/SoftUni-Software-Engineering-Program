user_points = {}
language_submissions = {}

data = input()

while data != 'exam finished':
    data = data.split('-')
    if data[1] == 'banned':
        user = data[0]
        del user_points[user]
    else:
        user, language, points = data
        points = int(points)
        if user in user_points:
            if user_points[user] < points:
                user_points[user] = points
        else:
            user_points[user] = points

        if language not in language_submissions:
            language_submissions[language] = 0
        language_submissions[language] += 1

    data = input()

print('Results:')
for user, points in user_points.items():
    print(f'{user} | {points}')
print('Submissions:')
for lang, submissions in language_submissions.items():
    print(f'{lang} - {submissions}')
