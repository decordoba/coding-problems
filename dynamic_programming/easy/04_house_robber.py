"""
Url: https://leetcode.com/explore/interview/card/top-interview-questions-easy/97/dynamic-programming/576/
Title: House Robber
Official difficulty: Easy
Real difficulty: 6/10

Description:
    You are a professional robber planning to rob houses along a street. Each house has a certain
    amount of money stashed, the only constraint stopping you from robbing each of them is that
    adjacent houses have security systems connected and it will automatically contact the police
    if two adjacent houses were broken into on the same night.

    Given an integer array nums representing the amount of money of each house, return the maximum
    amount of money you can rob tonight without alerting the police.

Example 1:
    Input: nums = [1,2,3,1]
    Output: 4
    Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
        Total amount you can rob = 1 + 3 = 4.

Example 2:
    Input: nums = [2,7,9,3,1]
    Output: 12
    Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
        Total amount you can rob = 2 + 9 + 1 = 12.

Constraints:
    1 <= nums.length <= 100
    0 <= nums[i] <= 400
"""


from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [0] * len(nums)
        for i, n in enumerate(nums):
            if i > 2:
                dp[i] = max(n + dp[i - 1], n + dp[i - 2])
            elif i == 2:
                dp[i] = n + dp[i - 2]
            else:
                dp[i] = n
        return max(dp)

    def rob_constant_space(self, nums: List[int]) -> int:
        prev1 = 0  # max if rob 1 house to the left
        prev2 = 0  # max if rob 2 houses to the left
        prev3 = 0  # max if rob 3 houses to the left
        for n in nums:
            curr = max(n + prev2, n + prev3)
            prev3 = prev2
            prev2 = prev1
            prev1 = curr
        return max(prev1, prev2)

    def rob_best(self, nums: list[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        prev1 = nums[0]
        prev2 = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            curr = max(prev2, prev1 + nums[i])
            prev1, prev2 = prev2, curr
        return prev2
