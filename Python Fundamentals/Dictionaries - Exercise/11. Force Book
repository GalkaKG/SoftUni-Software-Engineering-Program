def create_force_side(side, member, user_info_dict):
    condition = [current_side for current_side in user_info_dict if member in user_info_dict[current_side]]

    if len(condition) == 0:
        if side not in user_info_dict:
            user_info_dict[side] = [member]
        else:
            user_info_dict[side].append(member)

    return user_info_dict


def create_force_user(member, side, user_info_dict):
    for current_side in user_info_dict:
        if member in user_info_dict[current_side]:
            if len(user_info_dict[current_side]) > 1:
                user_info_dict[current_side].pop(member)
                break
            else:
                del user_info_dict[current_side]
                break

    if side in user_info_dict:
        user_info_dict[side].append(member)
    else:
        user_info_dict[side] = [member]

    print(f'{member} joins the {side} side!')


def force_book():
    user_info_dict = {}

    while True:
        command = input()
        if command == 'Lumpawaroo':
            break

        if '|' in command:
            command = command.split(' | ')
            side = command[0]
            member = command[1]
            create_force_side(side, member, user_info_dict)

        elif '->' in command:
            command = command.split(' -> ')
            member = command[0]
            side = command[1]
            create_force_user(member, side, user_info_dict)

    for data in user_info_dict:
        print(f'Side: {data}, Members: {len(user_info_dict[data])}')
        for name in user_info_dict[data]:
            print(f'! {name}')


force_book()
