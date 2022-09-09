# Bubble sort is a sorting algorithm that compares two adjacent elements and swaps them until they are in the intended order.

# Just like the movement of air bubbles in the water that rise up to the surface, each element of the array move to the end in each iteration.
# Therefore, it is called a bubble sort.

# You can change > to < to sort in descending order.


def bubble_sort(lst):
    for i in range(len(lst)):
        for j in range(len(lst) - 1 - i):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
    return lst


lst = [12, 1, 8, 17, 2]
print(bubble_sort(lst))
