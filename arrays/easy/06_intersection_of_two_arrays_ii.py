"""
Url: https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/674/
Title: Intersection of Two Arrays II
Official difficulty: Easy
Real difficulty: 5/10

Description:
    Given two integer arrays nums1 and nums2, return an array of their intersection.
    Each element in the result must appear as many times as it shows in both arrays,
    and you may return the result in any order.

Example 1:
    Input: nums1 = [1,2,2,1], nums2 = [2,2]
    Output: [2,2]

Example 2:
    Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
    Output: [4,9]
    Explanation: [9,4] is also accepted.

Constraints:
    1 <= nums1.length, nums2.length <= 1000
    0 <= nums1[i], nums2[i] <= 1000

Follow up:
    * What if the given array is already sorted? How would you optimize your algorithm?
    * What if nums1's size is small compared to nums2's size? Which algorithm is better?
    * What if elements of nums2 are stored on disk, and the memory is limited such that
      you cannot load all elements into the memory at once?
    """

from typing import List


class Solution:
    def intersect_slow(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """O(n1*n2)."""
        r = []
        for n in nums1:
            try:
                idx = nums2.index(n)
                nums2[idx] = None
                r.append(n)
            except ValueError:
                continue
        return r

    def intersect_mid(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """O(n1*log(n1) + n2*lon(n2))."""
        r = []
        nums1.sort()
        nums2.sort()
        i1, i2 = 0, 0
        while i1 < len(nums1) and i2 < len(nums2):
            n1 = nums1[i1]
            n2 = nums2[i2]
            if n1 == n2:
                r.append(n1)
                i1 += 1
                i2 += 1
            elif n1 < n2:
                i1 += 1
            else:
                i2 += 1
        return r

    def intersect_fast(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """O(n1 + n2)."""
        r = []
        d1 = {}
        for n in nums1:
            if n not in d1:
                d1[n] = 1
            else:
                d1[n] += 1
        d2 = {}
        for n in nums2:
            if n not in d2:
                d2[n] = 1
            else:
                d2[n] += 1
        if len(d1) > len(d2):
            d1, d2 = d2, d1
        for n in d1:
            if n not in d2:
                continue
            r += [n] * min(d1[n], d2[n])
        return r

    def intersect_short_nums1(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """Dict only for nums1."""
        r = []
        d1 = {}
        for n in nums1:
            if n not in d1:
                d1[n] = 1
            else:
                d1[n] += 1
        for n in nums2:
            if n in d1:
                r.append(n)
                d1[n] -= 1
                if d1[n] == 0:
                    del d1[n]
        return r

    def intersect_pythonic(self, nums1: List[int], nums2: List[int]) -> List[int]:
        from collections import Counter

        counts1 = Counter(nums1)
        counts2 = Counter(nums2)
        intersection = counts1 & counts2
        return list(intersection.elements())
