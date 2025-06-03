"""
Url: https://leetcode.com/explore/interview/card/top-interview-questions-medium/107/linked-list/783/
Title: Add Two Numbers
Official difficulty: Medium
Real difficulty: 5/10

Description:
    You are given two non-empty linked lists representing two non-negative integers.
    The digits are stored in reverse order, and each of their nodes contains a single digit.
    Add the two numbers and return the sum as a linked list.

    You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example 1:
    Input: l1 = [2,4,3], l2 = [5,6,4]
    Output: [7,0,8]
    Explanation: 342 + 465 = 807.

Example 2:
    Input: l1 = [0], l2 = [0]
    Output: [0]

Example 3:
    Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
    Output: [8,9,9,9,0,0,0,1]

Constraints:
    The number of nodes in each linked list is in the range [1, 100].
    0 <= Node.val <= 9
    It is guaranteed that the list represents a number that does not have leading zeros.
"""


from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # if a number is 0, return the other
        if l2 is None or l1 is None:
            return l1 if l2 is None else l2
        # add numbers and track carry
        carry = 0
        prev = ListNode(next=l1)
        while prev.next is not None and l2 is not None:
            prev.next.val += l2.val + carry
            if prev.next.val > 9:
                prev.next.val -= 10
                carry = 1
            else:
                carry = 0
            prev = prev.next
            l2 = l2.next
        # if one of the numbers still has numbers, append them
        if l2 is not None:
            prev.next = l2
        # solve carry if necessary
        while prev.next is not None and carry == 1:
            prev.next.val += carry
            if prev.next.val > 9:
                prev.next.val -= 10
                carry = 1
            else:
                carry = 0
            prev = prev.next
        # add carry if needed
        if carry == 1:
            prev.next = ListNode(val=1)
        return l1

    def addTwoNumbers_new_linkedlist(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        current = dummy
        carry = 0
        while l1 or l2 or carry:
            val = (l1.val if l1 else 0) + (l2.val if l2 else 0) + carry
            carry = val // 10
            val = val % 10
            current.next = ListNode(val)
            current = current.next
            l1 = l1.next if l1 else l1
            l2 = l2.next if l2 else l2
        return dummy.next
