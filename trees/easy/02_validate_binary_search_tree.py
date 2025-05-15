"""
Url: https://leetcode.com/explore/interview/card/top-interview-questions-easy/94/trees/625/
Title: Validate Binary Search Tree
Official difficulty: Easy
Real difficulty: 6/10

Description:
    Given the root of a binary tree, determine if it is a valid binary search tree (BST).

    A valid BST is defined as follows:
    * The left subtree of a node contains only nodes with keys less than the node's key.
    * The right subtree of a node contains only nodes with keys greater than the node's key.
    * Both the left and right subtrees must also be binary search trees.

Example 1:
    Input: root = [2,1,3]
    Output: true

Example 2:
    Input: root = [5,1,4,null,null,3,6]
    Output: false
    Explanation: The root node's value is 5 but its right child's value is 4.

Constraints:
    The number of nodes in the tree is in the range [1, 10^4].
    -2^31 <= Node.val <= 2^31 - 1
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
    def isValidBST_recursive(self, root: Optional[TreeNode]) -> bool:

        def tree_is_valid(root, minv=None, maxv=None):
            if root is None:
                return True
            if (maxv is not None and root.val >= maxv) or (minv is not None and root.val <= minv):
                return False
            return tree_is_valid(root.left, minv, root.val) and tree_is_valid(root.right, root.val, maxv)

        return tree_is_valid(root)

    def isValidBST_iterative(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        queue = deque([(root, None, None)])
        while queue:
            node, minv, maxv = queue.popleft()
            if minv is not None and node.val <= minv:
                return False
            if maxv is not None and node.val >= maxv:
                return False
            if node.left is not None:
                queue.append((node.left, minv, node.val))
            if node.right is not None:
                queue.append((node.right, node.val, maxv))
        return True
