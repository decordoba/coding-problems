"""
Url: https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/646/
Title: Rotate Array
Official difficulty: Easy
Real difficulty: 5/10

Description:
    Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.

Example 1:
    Input: nums = [1,2,3,4,5,6,7], k = 3
    Output: [5,6,7,1,2,3,4]
    Explanation:
        rotate 1 step to the right: [7,1,2,3,4,5,6]
        rotate 2 steps to the right: [6,7,1,2,3,4,5]
        rotate 3 steps to the right: [5,6,7,1,2,3,4]

Example 2:
    Input: nums = [-1,-100,3,99], k = 2
    Output: [3,99,-1,-100]
    Explanation:
        rotate 1 step to the right: [99,-1,-100,3]
        rotate 2 steps to the right: [3,99,-1,-100]

Constraints:
    1 <= nums.length <= 10^5
    -2^31 <= nums[i] <= 2^31 - 1
    0 <= k <= 10^5

Follow-up:
    Try to come up with as many solutions as you can.
    There are at least three different ways to solve this problem.
    Could you do it in-place with O(1) extra space?
"""

from typing import List


class Solution:
    def rotate_extra_space(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        N = len(nums)
        k = k % N
        if k == 0:
            return
        tmp_nums = nums[-k:].copy()
        for i in range(N - k - 1, -1, -1):
            nums[i + k] = nums[i]
        for i in range(k):
            nums[i] = tmp_nums[i]

    def rotate_in_place(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        N = len(nums)
        if N == 0:
            return
        k = k % N
        if k == 0:
            return
        count = N
        first_idx = N - 1
        idx = first_idx
        save = nums[idx]
        while count > 0:
            count -= 1
            if idx - k >= 0:
                nums[idx] = nums[idx - k]
                idx -= k
            elif N + idx - k == first_idx:
                nums[idx] = save
                first_idx -= 1
                idx = first_idx
                save = nums[idx]
            else:
                nums[idx] = nums[N + idx - k]
                idx = N + idx - k

    def rotate_with_reverse(self, nums, k):
        N = len(nums)
        if N == 0:
            return
        k = k % N
        if k == 0:
            return

        def reverse(nums, start, end):
            for i in range(int((end - start) / 2)):
                nums[start + i], nums[end - i - 1] = nums[end - i - 1], nums[start + i]

        def reverse_two_indices(start: int, end: int) -> None:
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1

        reverse(nums, 0, N)
        reverse(nums, 0, k)
        reverse(nums, k, N)
