"""
Url: https://leetcode.com/explore/interview/card/top-interview-questions-medium/107/linked-list/784/
Title: Odd Even Linked List
Official difficulty: Medium
Real difficulty: 5/10

Description:
    Given the head of a singly linked list, group all the nodes with odd indices together followed
    by the nodes with even indices, and return the reordered list.

    The first node is considered odd, and the second node is even, and so on.

    Note that the relative order inside both the even and odd groups should remain as it was in the input.

    You must solve the problem in O(1) extra space complexity and O(n) time complexity.

Example 1:
    Input: head = [1,2,3,4,5]
    Output: [1,3,5,2,4]

Example 2:
    Input: head = [2,1,3,5,6,4,7]
    Output: [2,3,6,7,1,5,4]

Constraints:
    The number of nodes in the linked list is in the range [0, 10^4].
    -10^6 <= Node.val <= 10^6
"""


from typing import Optional


# Definition for singly-linked list
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        odd = ListNode()
        even = ListNode()
        curr_odd = odd
        curr_even = even
        is_odd = True
        while head:
            if is_odd:
                curr_odd.next = head
                curr_odd = head
            else:
                curr_even.next = head
                curr_even = head
            is_odd = not is_odd
            head = head.next
        curr_odd.next = even.next
        curr_even.next = None
        return odd.next

    def oddEvenList_no_dummy_nodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        odd = head
        even = head.next
        even_head = even

        # two by two, replace odd by even
        while even and even.next:
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next

        odd.next = even_head
        return head
