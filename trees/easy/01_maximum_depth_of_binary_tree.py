"""
Url: https://leetcode.com/explore/interview/card/top-interview-questions-easy/94/trees/555/
Title: Maximum Depth of Binary Tree
Official difficulty: Easy
Real difficulty: 4/10

Description:
    Given the root of a binary tree, return its maximum depth.

    A binary tree's maximum depth is the number of nodes along the longest path from the
    root node down to the farthest leaf node.

Example 1:
    Input: root = [3,9,20,null,null,15,7]
    Output: 3

Example 2:
    Input: root = [1,null,2]
    Output: 2

Constraints:
    The number of nodes in the tree is in the range [0, 10^4].
    -100 <= Node.val <= 100
"""

from typing import Optional
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth_iterative(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        stack = [(1, root)]
        max_depth = 0
        while len(stack) > 0:
            depth, node = stack.pop()
            max_depth = max(depth, max_depth)
            if node.left is not None:
                stack.append((depth + 1, node.left))
            if node.right is not None:
                stack.append((depth + 1, node.right))
        return max_depth

    def maxDepth_recursive(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

    def maxDepth_bfs(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        depth = 0
        queue = deque([root])
        while len(queue) > 0:
            depth += 1
            level_size = len(queue)
            for _ in range(level_size):
                node = queue.popleft()
                if node.left is not None:
                    queue.append(node.left)
                if node.right is not None:
                    queue.append(node.right)
        return depth
