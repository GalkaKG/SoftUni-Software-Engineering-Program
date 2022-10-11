def create(n):
    if n == 1:
        return [0]
    if n == 0:
        return []
    result = [0, 1]
    for _ in range(n - 2):
        result.append(result[-1] + result[-2])
    return result


def locate(target, nums):
    for idx in range(len(nums)):
        curr_num = nums[idx]
        if curr_num == target:
            return idx
    return -1
