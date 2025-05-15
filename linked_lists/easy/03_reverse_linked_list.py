"""
Url: https://leetcode.com/explore/interview/card/top-interview-questions-easy/93/linked-list/560/
Title: Reverse Linked List
Official difficulty: Easy
Real difficulty: 7/10

Description:
    Given the head of a singly linked list, reverse the list, and return the reversed list.

Example 1:
    Input: head = [1,2,3,4,5]
    Output: [5,4,3,2,1]

Example 2:
    Input: head = [1,2]
    Output: [2,1]

Example 3:
    Input: head = []
    Output: []

Constraints:
    The number of nodes in the list is in the range [0, 5000].
    -5000 <= Node.val <= 5000

Follow-up:
    A linked list can be reversed either iteratively or recursively. Could you implement both?
"""
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList_iterative(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head
        nxt = head.next
        head.next = None
        while nxt is not None:
            prev = head
            head = nxt
            nxt = head.next
            head.next = prev
        return head

    def reverseList_iterative_improved(self, head: ListNode) -> ListNode:
        prev = None
        current = head

        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node

        return prev

    def reverseList_recursive(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None

        def reverse_list(node):
            if node.next is None:
                new_head = node
                return node, new_head
            parent_node, new_head = reverse_list(node.next)
            parent_node.next = node
            return node, new_head

        node, new_head = reverse_list(head)
        node.next = None
        return new_head

    def reverseList_recursive_improved(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head

        new_head = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return new_head
