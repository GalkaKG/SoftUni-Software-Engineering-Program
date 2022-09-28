from collections import deque


def best_list_pureness(nums, rotate_times):
    nums = deque(nums)
    sum_nums_data = {}
    for i in range(rotate_times + 1):
        sum_nums = 0
        for idx, num in enumerate(nums):
            sum_nums += num * idx
        nums.rotate()
        sum_nums_data[i] = sum_nums

    for k, v in sorted(sum_nums_data.items(), key=lambda x: -x[1]):
        return f'Best pureness {v} after {k} rotations'
