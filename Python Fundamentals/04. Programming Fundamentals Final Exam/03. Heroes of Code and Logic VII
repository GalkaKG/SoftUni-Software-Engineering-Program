def cast_spell(name_hero, needed_mp, spell, mp_dict):
    if mp_dict[name_hero] >= needed_mp:
        mp_dict[name_hero] -= needed_mp
        print(f"{name_hero} has successfully cast {spell} and now has {mp_dict[name_hero]} MP!")
    else:
        print(f"{name_hero} does not have enough MP to cast {spell}!")


def take_damage(name_hero, damage, attacker, hp_dict):
    hp_dict[name_hero] -= damage
    if hp_dict[name_hero] > 0:
        print(f'{name_hero} was hit for {damage} HP by {attacker} and now has {hp_dict[name_hero]} HP left!')
    else:
        del hp_dict[name_hero]
        print(f'{name_hero} has been killed by {attacker}!')


def recharge(name_hero, amount, mp_dict):
    diff = 200 - mp_dict[name_hero]
    mp_dict[name_hero] += amount
    amount_recovered = 0
    if mp_dict[name_hero] > 200:
        mp_dict[name_hero] = 200
        amount_recovered = diff
    else:
        amount_recovered = amount
    print(f'{name_hero} recharged for {amount_recovered} MP!')


def heal(name_hero, amount, hp_dict):
    diff = 100 - hp_dict[name_hero]
    hp_dict[name_hero] += amount
    if hp_dict[name_hero] > 100:
        hp_dict[name_hero] = 100
        amount_recovered = diff
    else:
        amount_recovered = amount
    print(f'{name_hero} healed for {amount_recovered} HP!')


def heroes_commands(heroes_hp, heroes_mp):
    while True:
        command = input()
        if command == 'End':
            break
        command = command.split(' - ')
        hero_name = command[1]
        if 'CastSpell' in command:
            mp_needed = int(command[2])
            spell_name = command[3]
            cast_spell(hero_name, mp_needed, spell_name, heroes_mp)
        elif 'TakeDamage' in command:
            damage = int(command[2])
            attacker = command[3]
            take_damage(hero_name, damage, attacker, heroes_hp)
        elif 'Recharge' in command:
            amount = int(command[2])
            recharge(hero_name, amount, heroes_mp)
        elif 'Heal' in command:
            amount = int(command[2])
            heal(hero_name, amount, heroes_hp)


def heroes():
    n = int(input())
    heroes_hp = {}
    heroes_mp = {}

    for _ in range(n):
        input_line = input().split()
        hero_name = input_line[0]
        hp = int(input_line[1])
        mp = int(input_line[2])
        heroes_hp[hero_name] = hp
        heroes_mp[hero_name] = mp
    heroes_commands(heroes_hp, heroes_mp)

    for k, v in heroes_hp.items():
        print(f'{k}\n HP: {v}\n MP: {heroes_mp[k]}')


heroes()
