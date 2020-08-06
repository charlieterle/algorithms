# Charles Dieterle
# Quicksort - first element pivot
# 27 August 2019
# edited 28 July 2019

def quicksort(arr):
    """
    Sort an array with the quicksort algorithm.
    args: arr - a list of numbers

    Note: this implementation chooses the first element of the array
    as the pivot element. This is not usually the best choice. See other
    quicksort files in this directory for other implementations.
    """

    def helper(arr, left, right):
        # left and right are indices that determine sub-arrays for
        # recursive calls so that quicksort can act in place

        arr_len = right - left
        if arr_len == 0 or arr_len == 1:
            return
        else:
            # choose first element as the pivot
            pivot = arr[left]

            # keep track of dividing point with i
            i = left + 1
            for j in range(i, right):
                if arr[j] < pivot:
                    arr[i], arr[j] = arr[j], arr[i]
                    i += 1

            # move pivot to the dividing point
            arr[left], arr[i - 1] = arr[i - 1], arr[left]

            # recursive calls to left and right sides
            helper(arr, left, i - 1)
            helper(arr, i, right)

    helper(arr, 0, len(arr))
    return arr


# tests
print(quicksort([]) == [],
    quicksort([7]) == [7],
    quicksort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5],
    quicksort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5],
    quicksort([3, 1, 4, 2, 5]) == [1, 2, 3, 4, 5],
    quicksort([4, 2, 1, 3, 6, 5, 7]) == [1, 2, 3, 4, 5, 6, 7],
    quicksort([7, 5, 3, 1, 6, 4, 2]) == [1, 2, 3, 4, 5, 6, 7],
    quicksort([5, 6, 8, 23, 4, 35, 12, 10, 3, 43, -4, 2, 3, 99, 20, 1]) == \
        [-4, 1, 2, 3, 3, 4, 5, 6, 8, 10, 12, 20, 23, 35, 43, 99],
)
