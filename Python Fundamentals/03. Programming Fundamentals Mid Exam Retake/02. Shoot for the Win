integers_list = list(map(int, input().split()))
command = input()
count_shoot_targets = 0
list_indexes = []

while command != 'End':
    index = int(command)

    if index+1 > len(integers_list):
        command = input()
        continue

    if index not in list_indexes:
        list_indexes.append(index)
        num_on_the_index = integers_list[index]
        current_target = - 1
        count_shoot_targets += 1
        integers_list[index] = current_target

        for i in range(len(integers_list)):
            if integers_list[i] <= num_on_the_index and integers_list[i] != -1:
                integers_list[i] = integers_list[i] + num_on_the_index
            elif integers_list[i] > num_on_the_index and integers_list != -1:
                integers_list[i] = integers_list[i] - num_on_the_index

    command = input()

str_integer_list = list(map(str, integers_list))
print(f'Shot targets: {count_shoot_targets} -> {" ".join(str_integer_list)}')
