"""
Url: https://leetcode.com/explore/interview/card/top-interview-questions-easy/94/trees/627/
Title: Symmetric Tree
Official difficulty: Easy
Real difficulty: 5/10

Description:
    Given the root of a binary tree, check whether it is a mirror of itself
    (i.e., symmetric around its center).

Example 1:
    Input: root = [1,2,2,3,4,4,3]
    Output: true

Example 2:
    Input: root = [1,2,2,null,3,null,3]
    Output: false

Constraints:
    The number of nodes in the tree is in the range [1, 1000].
    -100 <= Node.val <= 100

Follow-up:
    Could you solve it both recursively and iteratively?
"""

from collections import deque
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric_iterative(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        if root.left is None and root.right is None:
            return True
        queue = deque([root.left, root.right])
        while queue:
            size_level = len(queue)
            # split level in 2 sizes
            left = []
            for _ in range(size_level // 2):
                left.append(queue.popleft())
            right = []
            for _ in range(size_level // 2):
                right.append(queue.popleft())
            # compare left and reverse right
            for lt, rt in zip(left, right.reverse()):
                if lt.val != rt.val:
                    return False
                if lt.left is None and rt.right is not None:
                    return False
                if lt.left is not None and rt.right is None:
                    return False
                if lt.right is None and rt.left is not None:
                    return False
                if lt.right is not None and rt.left is None:
                    return False
            # add next level
            for node in left:
                if node.left is not None:
                    queue.append(node.left)
                if node.right is not None:
                    queue.append(node.right)
            for node in right:
                if node.left is not None:
                    queue.append(node.left)
                if node.right is not None:
                    queue.append(node.right)
        return True

    def isSymmetric_iterative_improved(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        queue = deque([root.left, root.right])
        while queue:
            left = queue.popleft()
            right = queue.popleft()
            if left is None and right is None:
                continue
            elif left is None or right is None or left.val != right.val:
                return False
            queue.append(left.left)
            queue.append(right.right)
            queue.append(left.right)
            queue.append(right.left)
        return True

    def isSymmetric_recursive(self, root: Optional[TreeNode]) -> bool:
        def symmetric(left, right):
            if left is None:
                return right is None
            elif right is None:
                return False
            elif left.val != right.val:
                return False
            return symmetric(left.left, right.right) and symmetric(left.right, right.left)

        def symmetric2(left, right):
            if left is None and right is None:
                return True
            elif right is None or left is None or left.val != right.val:
                return False
            return symmetric(left.left, right.right) and symmetric(left.right, right.left)

        if root is None:
            return True
        return symmetric(root.left, root.right)
