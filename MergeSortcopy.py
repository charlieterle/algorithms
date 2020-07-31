# Charles Dieterle
# Merge Sort
# 9 August 2019
# edited 26 July 2020

def merge_sort(list_of_nums):
    """
    Return a sorted list of numbers
    args: list_of_nums - list of numbers
    """
    list_len = len(list_of_nums)
    if list_len == 0:
        return []
    elif list_len == 1:
        return list_of_nums
    else:
        split = int(list_len / 2)

    # Split the list down the middle into sub-lists "left" & "right"
    left = merge_sort(list_of_nums[:split])
    right = merge_sort(list_of_nums[split:])

    # Initialize counters that will scan the sub-lists
    i = 0
    j = 0

    # Merge left & right into one list, "merged"
    merged = []
    for k in range(0, list_len):
        if i >= len(left):
            merged.extend(right[j:])
            break
        elif j >= len(right):
            merged.extend(left[i:])
            break
        elif left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    return merged

#tests
print(
    merge_sort([1]) == [1],
    merge_sort([-1.5, 2]) == [-1.5, 2],
    merge_sort([1.5, -2]) == [-2, 1.5],
    merge_sort([1, 2, 3, 4]) == [1, 2, 3, 4],
    merge_sort([4, 3, 2, 1]) == [1, 2, 3, 4],
    merge_sort([0, 0, 0, 0, 0, 0]) == [0, 0, 0, 0, 0, 0],
    merge_sort([3, 4, 1.2, 2]) == [1.2, 2, 3, 4],
    merge_sort([3, 4, 4, 3]) == [3, 3, 4, 4],
    merge_sort([3, 4, 5, 6, 7, 8.7, 9, 10]) == [3, 4, 5, 6, 7, 8.7, 9, 10],
    merge_sort([6, 7, 8, 9, 10, 1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    merge_sort([1, 4, 6.5, 2, 75, 64, 32, 3, 8]) == [1, 2, 3, 4, 6.5, 8, 32, 64, 75],
    merge_sort([-1, 5, 7, -3, 0]) == [-3, -1, 0, 5, 7],
    merge_sort([]) == [],
)
