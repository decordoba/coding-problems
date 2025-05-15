"""
Url: https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/567/
Title: Move Zeroes
Official difficulty: Easy
Real difficulty: 3/10

Description:
    Given an integer array nums, move all 0's to the end of it while maintaining the relative
    order of the non-zero elements.

    Note that you must do this in-place without making a copy of the array.

Example 1:
    Input: nums = [0,1,0,3,12]
    Output: [1,3,12,0,0]

Example 2:
    Input: nums = [0]
    Output: [0]

Constraints:
    1 <= nums.length <= 10^4
    -2^31 <= nums[i] <= 2^31 - 1

Follow-up:
    Could you minimize the total number of operations done?
"""

from typing import List


class Solution:
    def moveZeroes_zero_count(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        z = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                z += 1
            # else:
            elif z > 0:  # reduce writes
                nums[i - z] = nums[i]
        for i in range(1, z + 1):
            nums[-i] = 0

    def moveZeroes_two_indices(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        pos = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[pos] = nums[i]
                pos += 1
        for i in range(pos, len(nums)):
            nums[i] = 0
