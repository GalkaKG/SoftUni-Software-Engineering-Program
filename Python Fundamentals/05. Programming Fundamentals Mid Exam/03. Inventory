items_list = input().split(', ')

while True:
    command = input().split(' - ')

    if command[0] == 'Craft!':
        break

    item = command[1]

    if 'Collect' in command:
        if item not in items_list:
            items_list.append(item)
    elif 'Drop' in command:
        if item in items_list:
            items_list.remove(item)
    elif 'Combine Items' in command:
        items = item.split(':')
        old_item = items[0]
        new_item = items[1]
        if old_item in items_list:
            index_old_item = items_list.index(old_item)
            items_list.insert(index_old_item+1, new_item)
    elif 'Renew' in command:
        if item in items_list:
            items_list.remove(item), items_list.append(item)

print(', '.join(items_list))
