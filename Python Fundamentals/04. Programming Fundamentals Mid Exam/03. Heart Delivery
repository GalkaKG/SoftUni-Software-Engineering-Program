def representation_data(data, last_position):
    result = [x for x in data if x == 0]
    print(f"Cupid's last position was {last_position}.")
    if len(result) != len(data):
        diff = abs(len(data)) - len(result)
        print(f"Cupid has failed {diff} places.")
    else:
        print(f"Mission was successful.")


def heart_delivery(data):
    current_index_position = 0
    cupid_last_position = 0

    while True:
        command = input().split(' ')

        if command[0] == 'Love!':
            break

        index = int(command[1]) + current_index_position

        if index >= len(data):
            index = 0

        if -1 < index < len(data):
            if data[index] > 0:
                data[index] -= 2
                if data[index] == 0:
                    print(f"Place {index} has Valentine's day.")
            else:
                print(f"Place {index} already had Valentine's day.")

        cupid_last_position = index
        current_index_position = index

    representation_data(data, cupid_last_position)


nums = list(map(int, input().split('@')))
heart_delivery(nums)
