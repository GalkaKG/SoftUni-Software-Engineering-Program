# 1-st decision
def merge_arrs(left, right):
    new_array = []
    left_idx = 0
    right_idx = 0

    while left_idx < len(left) and right_idx < len(right):
        if left[left_idx] < right[right_idx]:
            new_array.append(left[left_idx])
            left_idx += 1
        else:
            new_array.append(right[right_idx])
            right_idx += 1

    while left_idx < len(left):
        new_array.append(left[left_idx])
        left_idx += 1

    while right_idx < len(right):
        new_array.append(right[right_idx])
        right_idx += 1

    return new_array


def merge_sort(nums):
    if len(nums) == 1:
        return nums

    middle = len(nums) // 2
    return merge_arrs(merge_sort(nums[:middle]), merge_sort(nums[middle:]))


numbers = [int(x) for x in input().split()]
sorted_array = merge_sort(numbers)
print(*sorted_array)



# 2-nd decision
def merge_arrays(left, right):
    result = [None] * (len(left) + len(right))
    left_idx = 0
    right_idx = 0
    result_idx = 0

    while left_idx < len(left) and right_idx < len(right):
        if left[left_idx] < right[right_idx]:
            result[result_idx] = left[left_idx]
            left_idx += 1
        else:
            result[result_idx] = right[right_idx]
            right_idx += 1
        result_idx += 1

    while left_idx < len(left):
        result[result_idx] = left[left_idx]
        left_idx += 1
        result_idx += 1

    while right_idx < len(right):
        result[result_idx] = right[right_idx]
        right_idx += 1
        result_idx += 1

    return result


def merge_sort(nums):
    if len(nums) == 1:
        return nums

    mid_idx = len(nums) // 2
    left = nums[:mid_idx]
    right = nums[mid_idx:]

    return merge_arrays(merge_sort(left), merge_sort(right))


nums = [int(x) for x in input().split()]
result = merge_sort(nums)
print(*result, sep=" ")
