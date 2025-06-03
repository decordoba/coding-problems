"""
missing_ranges.py
Url: https://leetcode.com/problems/missing-ranges/
Title: Missing Ranges
Official difficulty: Easy
Real difficulty: 4/10

Description:
    Given a sorted integer array `nums`, where the range of elements are in the inclusive range [`lower`, `upper`],
    return its missing ranges.

    A number `x` is considered missing if `x` is in the range [`lower`, `upper`] and `x` is not in `nums`.

    Return the shortest sorted list of ranges that exactly covers all the missing numbers.
    That is, no element of `nums` is included in any of the ranges, and each missing number
    is covered by exactly one of the ranges.

    For example, given `nums = [0, 1, 3, 50, 75]`, `lower = 0` and `upper = 99`,
    return `["2", "4->49", "51->74", "76->99"]`.

Example:
    Input: nums = [0, 1, 3, 50, 75], lower = 0, upper = 99
    Output: ["2", "4->49", "51->74", "76->99"]

Constraints:
    - `0 <= nums.length <= 100`
    - `-2^31 <= lower <= upper <= 2^31 - 1`
    - All the values of `nums` are unique.
    - `nums` is sorted in ascending order.
"""

from typing import List


class Solution:
    def missingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        first_idx = lower
        r = []
        for n in nums:
            if first_idx < n:
                last_idx = n - 1
                r.append(f"{first_idx}" if first_idx == last_idx else f"{first_idx}->{last_idx}")
            first_idx = n + 1
        if first_idx <= upper:
            r.append(f"{first_idx}" if first_idx == upper else f"{first_idx}->{upper}")
        return r
