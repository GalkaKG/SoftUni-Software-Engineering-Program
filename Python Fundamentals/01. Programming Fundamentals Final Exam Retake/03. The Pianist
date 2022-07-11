n = int(input())
data = {}

for _ in range(n):
    piece, composer, key = input().split('|')
    data[piece] = [composer, key]

while True:
    command = input()

    if command == 'Stop':
        break

    command = command.split('|')

    if 'Add' in command:
        piece = command[1]
        composer = command[2]
        key = command[3]

        if piece not in data:
            data[piece] = [composer, key]
            print(f'{piece} by {composer} in {key} added to the collection!')
        else:
            print(f'{piece} is already in the collection!')

    elif 'Remove' in command:
        piece = command[1]
        if piece in data:
            del data[piece]
            print(f'Successfully removed {piece}!')
        else:
            print(f'Invalid operation! {piece} does not exist in the collection.')

    elif 'ChangeKey' in command:
        piece = command[1]
        new_key = command[2]
        if piece in data:
            data[piece][1] = new_key
            print(f'Changed the key of {piece} to {new_key}!')
        else:
            print(f'Invalid operation! {piece} does not exist in the collection.')

for k, v in data.items():
    print(f'{k} -> Composer: {v[0]}, Key: {v[1]}')
