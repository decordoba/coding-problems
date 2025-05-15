"""
Url: https://leetcode.com/explore/interview/card/top-interview-questions-easy/96/sorting-and-searching/587/
Title: Merge Sorted Array
Official difficulty: Easy
Real difficulty: 8/10

Description:
    You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two
    integers m and n, representing the number of elements in nums1 and nums2 respectively.

    Merge nums1 and nums2 into a single array sorted in non-decreasing order.

    The final sorted array should not be returned by the function, but instead be stored inside
    the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements
    denote the elements that should be merged, and the last n elements are set to 0 and should be
    ignored. nums2 has a length of n.

Example 1:
    Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
    Output: [1,2,2,3,5,6]
    Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
    The result of the merge is [1,2,2,3,5,6].

Example 2:
    Input: nums1 = [1], m = 1, nums2 = [], n = 0
    Output: [1]
    Explanation: The arrays we are merging are [1] and [].
    The result of the merge is [1].

Example 3:
    Input: nums1 = [0], m = 0, nums2 = [1], n = 1
    Output: [1]
    Explanation: The arrays we are merging are [] and [1].
    The result of the merge is [1].

Constraints:
    nums1.length == m + n
    nums2.length == n
    0 <= m, n <= 200
    1 <= m + n <= 200
    -10^9 <= nums1[i], nums2[j] <= 10^9

Follow-up:
    Can you come up with an algorithm that runs in O(m + n) time?
"""


from typing import List


class Solution:
    def merge_mine(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # put m elements of nums1 at the end of nums1
        for i in range(m - 1, -1, -1):
            nums1[n + i] = nums1[i]
        # take numbers from nums1 or nums2 and place them in nums1
        i = n
        j = 0
        k = 0
        while k < n + m and j < n and i < n + m:
            if nums1[i] < nums2[j]:
                nums1[k] = nums1[i]
                i += 1
            else:
                nums1[k] = nums2[j]
                j += 1
            k += 1
        # copy remaining elements
        for i in range(j, n):
            nums1[i + m] = nums2[i]

    def merge_better(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = m - 1
        j = n - 1
        k = n + m - 1
        while j >= 0 and i >= 0:
            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1
        while j >= 0:
            nums1[k] = nums2[j]
            j -= 1
            k -= 1

    def merge_bubble(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # Not optimal, O(n*m)
        i = 0
        while i < n:
            # put smallest number in nums1[i] and largest number in nums2[0] and advance i
            if nums1[i] > nums2[0]:
                nums1[i], nums2[0] = nums2[0], nums1[i]
            i += 1
            # bubble up larger number in nums2 to keep order
            j = 1
            while j < m:
                if nums2[j - 1] <= nums2[j]:
                    break
                nums2[j - 1], nums2[j] = nums2[j], nums2[j - 1]
                j += 1
        for i in range(m):
            nums1[n + i] = nums2[i]
