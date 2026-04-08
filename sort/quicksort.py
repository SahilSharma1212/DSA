def quickSort(arr):

    # Base case:
    # If the array has 0 or 1 element, it is already sorted
    if len(arr) <= 1:
        return arr

    # Choose the pivot element (middle element of the array)
    pivot = arr[len(arr) - 1]

    # # Create a list of elements smaller than the pivot
    left = [x for x in arr if x < pivot]

    # # Create a list of elements equal to the pivot
    middle = [x for x in arr if x == pivot]

    # # Create a list of elements greater than the pivot
    right = [x for x in arr if x > pivot]

    # Recursively sort the left and right parts
    # then combine them with the pivot values in the middle
    return quickSort(left) + middle + quickSort(right)


# Input array
arr = [38, 27, 43, 3, 9, 82, 10]

# Call quicksort
res = quickSort(arr)

# Print sorted result
print(res)