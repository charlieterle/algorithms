# Charles Dieterle
# Inversion counting in an array (utilizing merge sort)
# 20 August 2019
# edited 26 July 2020

def inversion_count(list_of_ints):
    """
    return an int equal to the number of inversions in arr
    arr - list of ints
    Definition of inversion:
    elements arr[i] and arr[j] form an inversion iff arr[i] > arr[j] and i < j
    """
    def merge_sort_and_count(arr, count):
        # helper function to keep track of inversions

        length = len(arr)

        if length == 0:
            return [], 0

        elif length == 1:
            return arr, 0

        split = int(length / 2)

        # sort each half and count inversions for those halves
        left_half, left_inv = merge_sort_and_count(arr[:split], count)
        right_half, right_inv = merge_sort_and_count(arr[split:], count)

        # indices to traverse the left and right halves
        i = 0
        j = 0

        # array to hold results of merging left & right halves
        merged = []

        # inversion count for this recursive call
        inv = 0

        for k in range(0, length):
            if i >= len(left_half):
                merged.extend(right_half[j:])
                break
            elif j >= len(right_half):
                merged.extend(left_half[i:])
                break
            elif left_half[i] <= right_half[j]:
                merged.append(left_half[i])
                i += 1
            else:
                merged.append(right_half[j])
                j += 1
                inv += len(left_half[i:])

        # return sorted array and total inversions from all recursive calls
        return merged, (left_inv + right_inv + inv)

    return merge_sort_and_count(list_of_ints, 0)

# tests
print(
    inversion_count([1]) == ([1], 0),
    inversion_count([1, 2]) == ([1, 2], 0),
    inversion_count([1, 2, 3, 4]) == ([1, 2, 3, 4], 0),
    inversion_count([4, 3, 2, 1]) == ([1, 2, 3, 4], 6),
    inversion_count([3, 4, 4, 3]) == ([3, 3, 4, 4], 2),
    inversion_count([3, 4, 5, 6, 7, 8, 9, 10]) == ([3, 4, 5, 6, 7, 8, 9, 10], 0),
    inversion_count([6, 7, 8, 9, 10, 1, 2, 3, 4, 5]) == ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 25),
    inversion_count([-1, 5, 7, -3, 0]) == ([-3, -1, 0, 5, 7], 5),
    inversion_count([]) == ([], 0),
)
