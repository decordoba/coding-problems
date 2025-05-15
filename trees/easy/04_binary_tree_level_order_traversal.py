"""
Url: https://leetcode.com/explore/interview/card/top-interview-questions-easy/94/trees/628/
Title: Binary Tree Level Order Traversal
Official difficulty: Easy
Real difficulty: 4/10

Description:
    Given the root of a binary tree, return the level order traversal of its nodes' values.
    (i.e., from left to right, level by level).

Example 1:
    Input: root = [3,9,20,null,null,15,7]
    Output: [[3],[9,20],[15,7]]

Example 2:
    Input: root = [1]
    Output: [[1]]

Example 3:
    Input: root = []
    Output: []

Constraints:
    The number of nodes in the tree is in the range [0, 2000].
    -1000 <= Node.val <= 1000
"""

from collections import deque
from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        r = []
        queue = deque([root]) if root is not None else deque([])
        while queue:
            size_level = len(queue)
            level = []
            for _ in range(size_level):
                node = queue.popleft()
                level.append(node.val)
                if node.left is not None:
                    queue.append(node.left)
                if node.right is not None:
                    queue.append(node.right)
            r.append(level)
        return r
