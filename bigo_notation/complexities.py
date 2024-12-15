# TODO: define the complexity of each function

def is_even(num):
    return num % 2 == 0


def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1


def count_down(n):
    while n > 1:
        n = n // 2
        print(n)


def print_all_elements(arr):
    for elem in arr:
        print(elem)


def print_pairs(arr):
    for i in arr:
        for j in arr:
            print(i, j)


def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]
        merge_sort(left_half)
        merge_sort(right_half)
        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1
        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1


def fibonacci_recursive(n):
    if n <= 1:
        return n
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


def power_set(arr):
    result = [[]]
    for elem in arr:
        new_subsets = [subset + [elem] for subset in result]
        result.extend(new_subsets)
    return result


def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)
