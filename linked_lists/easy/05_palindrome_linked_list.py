"""
Url: https://leetcode.com/explore/interview/card/top-interview-questions-easy/93/linked-list/772/
Title: Palindrome Linked List
Official difficulty: Easy
Real difficulty: 6/10

Description:
    Given the head of a singly linked list, return true if it is a palindrome or false otherwise.

Example 1:
    Input: head = [1,2,2,1]
    Output: true

Example 2:
    Input: head = [1,2]
    Output: false

Constraints:
    The number of nodes in the list is in the range [1, 10^5].
    0 <= Node.val <= 9

Follow-up:
    Could you do it in O(n) time and O(1) space?
"""

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # find half point in linked list
        dummy = ListNode(next=head)
        fast = slow = dummy
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        mid_point = slow.next
        # reverse second half
        prev = None
        node = mid_point
        while node is not None:
            nxt = node.next
            node.next = prev
            prev = node
            node = nxt
        end_point = prev
        # check palindrome
        palindrome = True
        first = head
        second = end_point
        while second is not None:
            if second.val != first.val:
                palindrome = False
                break
            first = first.next
            second = second.next
        # rebuild linked list second half (optional)
        prev = None
        node = end_point
        while node is not None:
            nxt = node.next
            node.next = prev
            prev = node
            node = nxt
        return palindrome
