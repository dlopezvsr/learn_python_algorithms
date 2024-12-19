"""
Description:
Given an array of integers nums and an integer k, find the maximum sum of any contiguous subarray of size k.

Input: nums = [2, 1, 5, 1, 3, 2], k = 3
Output: 9
Explanation: Subarray with a maximum sum is [5, 1, 3].

Input: nums = [2, 3, 4, 1, 5], k = 2
Output: 7
Explanation: Subarray with a maximum sum is [3, 4].
"""


def maxSubArray(nums, k):
    max_sum = float('-inf')

    for right in range(k, len(nums)):
        left = right - k
        max_sum = max(max_sum, nums[left:right + 1])

    return max_sum


nums = [2, 3, 4, 1, 5]
k = 2
maxSubArray(nums, k)
print(maxSubArray(nums, k))
