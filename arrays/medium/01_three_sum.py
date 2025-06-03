"""
Url: https://leetcode.com/explore/interview/card/top-interview-questions-medium/103/array-and-strings/776/
Title: 3Sum
Official difficulty: Easy
Real difficulty: 7/10

Description:
    Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that
    i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

    Notice that the solution set must not contain duplicate triplets.

Example 1:
    Input: nums = [-1,0,1,2,-1,-4]
    Output: [[-1,-1,2],[-1,0,1]]
    Explanation:
        The distinct triplets that sum to zero are [-1,0,1] and [-1,-1,2].

Example 2:
    Input: nums = [0,1,1]
    Output: []
    Explanation: No three numbers sum to zero.

Example 3:
    Input: nums = [0,0,0]
    Output: [[0,0,0]]
    Explanation: The only valid triplet is [0,0,0].

Constraints:
    3 <= nums.length <= 3000
    -10^5 <= nums[i] <= 10^5
"""

from collections import defaultdict
from typing import List


class Solution:
    def threeSum_seach(self, nums: List[int]) -> List[List[int]]:
        """Search string after ordering it."""
        n = len(nums)
        nums.sort()
        ret = []

        for i in range(n - 2):
            # skip if i is not in first pos of repeted numbers
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            # search from both sides for numbers
            left, right = i + 1, n - 1
            while left < right:
                result = nums[i] + nums[left] + nums[right]
                if result < 0:
                    left += 1
                elif result > 0:
                    right -= 1
                else:
                    ret.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    # skip all repeated numbers in left
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
        return ret

    def threeSum_slow(self, nums: List[int]) -> List[List[int]]:
        """Remove all numbers that appear more than 3 times, then 'brute' force with a dict."""
        # create ht with indices of numbers
        # remove repetitions of nums more than 3 times
        ht = {}
        new_nums = []
        for i, num in enumerate(nums):
            if num not in ht:
                ht[num] = []
            if len(ht[num]) < 3:
                ht[num].append(len(new_nums))
                new_nums.append(num)
        nums = new_nums
        n = len(nums)
        # sum all number pairs, and see if they match another number
        mem = set()
        for i in range(n):
            for j in range(i + 1, n):
                neg_sum = -(nums[i] + nums[j])
                if neg_sum in ht:
                    itm = tuple(sorted([nums[i], nums[j], neg_sum]))
                    if itm in mem:
                        continue
                    for pos in ht[neg_sum]:
                        if pos not in [i, j]:
                            mem.add(itm)
                            break
        return list(mem)

    def threeSum_simple(self, nums: List[int]) -> List[List[int]]:
        # group in positives, negatives and zeros
        neg = defaultdict(int)
        pos = defaultdict(int)
        zeros = 0
        for x in nums:
            if x < 0:
                neg[x] += 1
            elif x > 0:
                pos[x] += 1
            else:
                zeros += 1

        r = []

        # calculate responses with zeros
        if zeros:
            for n in neg:
                if -n in pos:
                    r.append((0, n, -n))

            if zeros > 2:
                r.append((0, 0, 0))

        # calculate responses without zeros
        for set_a, set_b in ((neg, pos), (pos, neg)):
            set_a_items = list(set_a.items())
            for i, (n1, q1) in enumerate(set_a_items):
                for n2, q2 in set_a_items[i:]:
                    if n1 != n2 or (n1 == n2 and q1 > 1):
                        if -n1 - n2 in set_b:
                            r.append((n1, n2, -n1 - n2))

        return r
