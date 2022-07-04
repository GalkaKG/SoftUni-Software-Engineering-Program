def array_sum(nums, idx):
    if idx == len(nums) - 1:
        return nums[idx]
    return nums[idx] + array_sum(nums, idx + 1)


nums = [int(x) for x in input().split()]

print(array_sum(nums, 0))
