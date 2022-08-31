# first decision:

nums = [int(x) for x in input().split()]

is_sorted = False
counter = 0
while not is_sorted:
    is_sorted = True
    for i in range(1, len(nums) - counter):
        if nums[i] < nums[i - 1]:
            nums[i], nums[i - 1] = nums[i - 1], nums[i]
            is_sorted = False
    counter += 1

print(*nums, sep=" ")





# second decision:

nums = [int(x) for x in input().split()]
for i in range(len(nums)):
    for j in range(1, len(nums) - i):
        if nums[j - 1] > nums[j]:
            nums[j], nums[j - 1] = nums[j - 1], nums[j]

print(*nums, sep=" ")
