"""
Url: https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/578/
Title: Contains Duplicate
Official difficulty: Easy
Real difficulty: 2/10

Description:
    Given an integer array nums, return true if any value appears at least twice in the array,
    and return false if every element is distinct.

Example 1:
    Input: nums = [1,2,3,1]
    Output: true
    Explanation: The element 1 occurs at the indices 0 and 3.

Example 2:
    Input: nums = [1,2,3,4]
    Output: false
    Explanation: All elements are distinct.

Example 3:
    Input: nums = [1,1,1,3,3,4,3,2,4,2]
    Output: true

Constraints:
    1 <= nums.length <= 10^5
    -10^9 <= nums[i] <= 10^9
"""

from typing import List


class Solution:
    def containsDuplicate1(self, nums: List[int]) -> bool:
        return not len(set(nums)) == len(nums)

    def containsDuplicate(self, nums: List[int]) -> bool:
        s = set()
        for n in nums:
            if n in s:
                return True
            s.add(n)
        return False
