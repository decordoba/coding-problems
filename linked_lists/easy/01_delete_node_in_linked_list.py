"""
Url: https://leetcode.com/explore/interview/card/top-interview-questions-easy/93/linked-list/553/
Title: Delete Node in a Linked List
Official difficulty: Easy
Real difficulty: 4/10

Description:
    There is a singly-linked list head and we want to delete a node node in it.

    You are given the node to be deleted node. You will not be given access to the first node of head.

    All the values of the linked list are unique, and it is guaranteed that the given node node
    is not the last node in the linked list.

    Delete the given node. Note that by deleting the node, we do not mean removing it from memory.
    We mean:
    * The value of the given node should not exist in the linked list.
    * The number of nodes in the linked list should decrease by one.
    * All the values before node should be in the same order.
    * All the values after node should be in the same order.

Example 1:
    Input: head = [4,5,1,9], node = 5
    Output: [4,1,9]
    Explanation: You are given the second node with value 5, the linked list should become 4 -> 1 -> 9
                 after calling your function.

Example 2:
    Input: head = [4,5,1,9], node = 1
    Output: [4,5,9]
    Explanation: You are given the third node with value 1, the linked list should become 4 -> 5 -> 9
                 after calling your function.

Constraints:
    The number of the nodes in the given list is in the range [2, 1000].
    -1000 <= Node.val <= 1000
    The value of each node in the list is unique.
    The node to be deleted is in the list and is not a tail node.
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteNode_slow(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        while node.next is not None:
            next_node = node.next
            # put value of next node into node
            node.val = next_node.val
            # if next_node is last, remove it and end
            if next_node.next is None:
                node.next = None
                del next_node
                break
            # repeat for next_node if not last
            else:
                node = next_node

    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val
        to_rm = node.next
        node.next = node.next.next
        del to_rm
