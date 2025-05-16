"""
Url: https://leetcode.com/explore/interview/card/top-interview-questions-easy/99/others/722/
Title: Missing Number
Official difficulty: Easy
Real difficulty: 2/10

Description:
    Given an array nums containing n distinct numbers in the range [0, n], return the only
    number in the range that is missing from the array.

Example 1:
    Input: nums = [3,0,1]
    Output: 2
    Explanation:
        n = 3 since there are 3 numbers, so all numbers are in the range [0,3].
        2 is the missing number since it does not appear in nums.

Example 2:
    Input: nums = [0,1]
    Output: 2
    Explanation:
        n = 2 since there are 2 numbers, so all numbers are in the range [0,2].
        2 is the missing number since it does not appear in nums.

Example 3:
    Input: nums = [9,6,4,2,3,5,7,0,1]
    Output: 8
    Explanation:
        n = 9, numbers range from 0 to 9. 8 is missing from nums.

Constraints:
    n == nums.length
    1 <= n <= 10^4
    0 <= nums[i] <= n
    All the numbers of nums are unique.

Follow-up:
    Could you implement a solution using only O(1) extra space complexity
    and O(n) runtime complexity?
"""


from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        sum_n = int((n + 1) * n / 2)
        return sum_n - sum(nums)

    def missingNumber_xor(self, nums: List[int]) -> int:
        r = len(nums)
        for i, n in enumerate(nums):
            r ^= i ^ n
        return r
