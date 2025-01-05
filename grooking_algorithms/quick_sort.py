# This is a recursive function,
# So quick sort needs a base case to stop.
# The formula is about keeping adding the values below the pivot + pivot + values above pivot
def quick_sort(arr):
    # Fisrt a base case is implemented: the array is 1 or less, so it does not need to be split anymore
    if len(arr) <= 1:
        return arr  # Return the array
    else:
        pivot = arr[-1]  # Select the pivot number that will be compared with every item, here we selected the last one
        below_pivot = [x for x in arr[:-1] if x <= pivot]  # List comprenhention to filter and select the numbers below
        # Important to notice that the last item is exclueded cuz is selected as pivot
        above_pivot = [x for x in arr[:-1] if x >= pivot]  # same as above but with numbers higher than pivot
        # Below you find the recursive case where the arrays are splited and quick-sorted again until base case is met
        return quick_sort(below_pivot) + [pivot] + quick_sort(above_pivot)


# Example usage:
arr = [10, 7, 8, 9, 1, 5]
sorted_arr = quick_sort(arr)
print("Sorted array is:", sorted_arr)


### Quick sort in-place

def quicksort(arr, low, high):
    if low < high:
        # Partition the array and get the pivot index
        pivot_index = partition(arr, low, high)

        # Recursively sort the left and right subarrays
        quicksort(arr, low, pivot_index - 1)
        quicksort(arr, pivot_index + 1, high)


def partition(arr, low, high):
    # Choose the last element as the pivot
    pivot = arr[high]
    i = low - 1  # Pointer for the smaller element

    for j in range(low, high):
        # If the current element is smaller than or equal to the pivot
        if arr[j] <= pivot:
            i += 1  # Move the pointer for the smaller element
            arr[i], arr[j] = arr[j], arr[i]  # Swap elements

    # Place the pivot in its correct position
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1  # Return the pivot index


# Example usage:
arr = [8, 3, 1, 7, 0, 10, 2]
quicksort(arr, 0, len(arr) - 1)
print("Sorted array:", arr)
