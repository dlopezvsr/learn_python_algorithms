
# To have a binary search function, you generally need to receive an array and the item to search.
# Also, to apply a binary search, have in mind that the array needs to be sorted
def binary_search(arr, target):
    left = 0  # this is the variable that point to the initial value (the very beginning of the array).
    right = len(arr) - 1  # this is the variable that points to the end of the array.

    while left <= right:  # while loop will be in charge of iterating until the minimum value is equals to maximum
        mid = left + right // 2
        # the mid-value needs it to be inside the while loop because it is changing with the iterations
        if target > arr[mid]:
            # if the target value falls on the right side, the beginning of the right side (left) has to be
            # the mid-value plus one
            left = mid + 1
        elif target < arr[mid]:
            # if the target value falls on the left side meaning is less than the mid one, the right value (the end)
            # has to be the mid minus one.
            right = mid - 1
        else:
            return mid
            # This means that in some of the previous conditions the mid value (index) is the same as target
            # causing that neither < nor > are encountered so else will return the index
    return -1


# Test cases
print(binary_search([1, 3, 5, 7, 9], 3))  # Output: 1
print(binary_search([1, 3, 5, 7, 9], 4))  # Output: -1
print(binary_search([1, 3, 5, 7, 9], 9))  # Output: 4
print(binary_search([1, 3, 5, 7, 9], 1))  # Output: 0
print(binary_search([1, 3, 5, 7, 9], 5))  # Output: 2
