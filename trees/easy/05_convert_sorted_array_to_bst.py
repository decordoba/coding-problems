"""
Url: https://leetcode.com/explore/interview/card/top-interview-questions-easy/94/trees/631/
Title: Convert Sorted Array to Binary Search Tree
Official difficulty: Easy
Real difficulty: 5/10

Description:
    Given an integer array nums where the elements are sorted in ascending order, convert it to
    a height-balanced binary search tree.

Example 1:
    Input: nums = [-10,-3,0,5,9]
    Output: [0,-3,9,-10,null,5]
    Explanation: [0,-10,5,null,-3,null,9] is also accepted.

Example 2:
    Input: nums = [1,3]
    Output: [3,1]
    Explanation: [1,null,3] and [3,1] are both height-balanced BSTs.

Constraints:
    1 <= nums.length <= 10^4
    -10^4 <= nums[i] <= 10^4
    nums is sorted in a strictly increasing order.
"""

from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def get_tree(nums, start, end):
            if start >= end:
                return TreeNode(nums[start])
            elif start == end - 1:
                return TreeNode(nums[start], right=TreeNode(nums[end]))
            mid = (end + start) // 2
            left = get_tree(nums, start, mid - 1)
            right = get_tree(nums, mid + 1, end)
            node = TreeNode(nums[mid], left, right)
            return node
        return get_tree(nums, 0, len(nums) - 1)

    def sortedArrayToBST_slightly_different(self, nums: List[int]) -> Optional[TreeNode]:
        def get_tree(nums, start, end):
            if start > end:
                return None
            mid = (end + start) // 2
            left = get_tree(nums, start, mid - 1)
            right = get_tree(nums, mid + 1, end)
            node = TreeNode(nums[mid], left, right)
            return node
        return get_tree(nums, 0, len(nums) - 1)
