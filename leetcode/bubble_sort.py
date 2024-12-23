"""
You are given a list of integers representing the scores of students in an exam. Your task is to:

- Sort the scores in descending order using the Bubble Sort algorithm.
- Return the top 3 scores from the sorted list. If there are fewer than 3 students,
  return all the scores in descending order.
"""


def bubble_sort(arr):
    for i in range(len(arr)):
        validator = False
        for j in range(0, len(arr) - i - 1):
            if arr[j] < arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                validator = True
        if not validator:
            break

    return arr[:3]


scores = [45, 78, 88, 32, 56, 99, 85]
scores2 = [50, 50, 50]
scores3 = [95]
print(bubble_sort(scores3))
