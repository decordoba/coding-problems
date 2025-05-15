"""
Url: https://leetcode.com/explore/interview/card/top-interview-questions-easy/93/linked-list/603/
Title: Remove Nth Node From End of List
Official difficulty: Easy
Real difficulty: 6/10

Description:
    Given the head of a linked list, remove the nth node from the end of the list and return its head.

Example 1:
    Input: head = [1,2,3,4,5], n = 2
    Output: [1,2,3,5]

Example 2:
    Input: head = [1], n = 1
    Output: []

Example 3:
    Input: head = [1,2], n = 1
    Output: [1]

Constraints:
    The number of nodes in the list is sz.
    1 <= sz <= 30
    0 <= Node.val <= 100
    1 <= n <= sz

Follow-up:
    Could you do this in one pass?
"""

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd_two_ptrs(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        ptr = ListNode(next=head)
        first = ptr
        for _ in range(n):
            first = first.next
            if first is None:
                return head
        second = ptr
        while first.next is not None:
            first = first.next
            second = second.next
        second.next = second.next.next
        return ptr.next

    def removeNthFromEnd_count(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        ptr = ListNode(next=head)
        node = ptr
        num = 0
        while node.next is not None:
            node = node.next
            num += 1
        node = ptr
        while num > n:
            node = node.next
            num -= 1
        node.next = node.next.next
        return ptr.next

    def removeNthFromEnd_two_ptrs_2(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(0, head)
        slow = fast = dummy

        # Move fast n + 1 steps ahead (so slow ends up before the node to remove)
        for _ in range(n + 1):
            fast = fast.next

        # Move both until fast reaches the end
        while fast:
            slow = slow.next
            fast = fast.next

        # Delete the nth node from end
        slow.next = slow.next.next

        return dummy.next
