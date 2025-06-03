"""
Url: https://leetcode.com/explore/interview/card/top-interview-questions-medium/103/array-and-strings/781/
Title: Increasing Triplet Subsequence
Official difficulty: Medium
Real difficulty: 5/10

Description:
    Given an integer array `nums`, return true if there exists a triple of indices (i, j, k)
    such that i < j < k and nums[i] < nums[j] < nums[k]. If no such indices exist, return false.

Example 1:
    Input: nums = [1,2,3,4,5]
    Output: true
    Explanation: Any triplet where i < j < k is valid.

Example 2:
    Input: nums = [5,4,3,2,1]
    Output: false
    Explanation: No triplet exists.

Example 3:
    Input: nums = [2,1,5,0,4,6]
    Output: true
    Explanation: The triplet (3, 4, 5) is valid because nums[3] == 0 < nums[4] == 4 < nums[5] == 6.

Constraints:
    1 <= nums.length <= 5 * 10^5
    -2^31 <= nums[i] <= 2^31 - 1

Follow-up:
    Could you implement a solution that runs in O(n) time complexity and O(1) space complexity?
"""


from typing import List


class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        if len(nums) < 3:
            return False
        r = [nums[0]]
        for n in nums[1:]:
            if n <= r[0]:
                r[0] = n
            elif len(r) == 1:
                r.append(n)
            elif n <= r[1]:
                r[1] = n
            else:
                return True
        return False
