"""
Url: https://leetcode.com/explore/interview/card/top-interview-questions-medium/107/linked-list/785/
Title: Intersection of Two Linked Lists
Official difficulty: Easy
Real difficulty: 5/10

Description:
    Given the heads of two singly linked-lists `headA` and `headB`, return the node at which the two lists intersect.
    If the two linked lists have no intersection at all, return null.

    The test cases are generated such that there are no cycles anywhere in the entire linked structure.

    Note that the linked lists must retain their original structure after the function returns.

    Custom Judge:
    The inputs to the judge are given as follows (your program is not given these inputs):

        - `intersectVal` - The value of the node where the intersection occurs. This is 0 if there is no intersected node.
        - `listA` - The first linked list.
        - `listB` - The second linked list.
        - `skipA` - The number of nodes to skip ahead in listA to get to the intersected node.
        - `skipB` - The number of nodes to skip ahead in listB to get to the intersected node.

    The judge will then create the linked structure based on these inputs and pass the two heads to your program.
    If you correctly return the intersected node, then your solution will be accepted.

Example 1:
    Input: intersectVal = 8, listA = [4,1,8,4,5], listB = [5,6,1,8,4,5], skipA = 2, skipB = 3
    Output: Intersected at '8'

Example 2:
    Input: intersectVal = 2, listA = [1,9,1,2,4], listB = [3,2,4], skipA = 3, skipB = 1
    Output: Intersected at '2'

Example 3:
    Input: intersectVal = 0, listA = [2,6,4], listB = [1,5], skipA = 3, skipB = 2
    Output: No intersection

Constraints:
    The number of nodes of listA is in the m.
    The number of nodes of listB is in the n.
    1 <= m, n <= 3 * 10^4
    1 <= Node.val <= 10^5
    0 <= skipA <= m
    0 <= skipB <= n
    intersectVal is 0 if listA and listB do not intersect.
    intersectVal == listA[skipA] == listB[skipB] if listA and listB intersect.

Follow-up:
    Could you write a solution that runs in O(m + n) time and use only O(1) memory?
"""


from typing import Optional


# Definition for singly-linked list
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        # count nodes until end in A and B
        curr = headA
        countA = 0
        while curr:
            curr = curr.next
            countA += 1
        curr = headB
        countB = 0
        while curr:
            curr = curr.next
            countB += 1
        # make sure headA has the most nodes
        if countA < countB:
            headA, headB = headB, headA
            countA, countB = countB, countA
        # position headA at same distance of tail as headB
        count = countB
        while count < countA:
            headA = headA.next
            count += 1
        # search for intersection
        while headA:
            if headA == headB:
                return headA
            headA = headA.next
            headB = headB.next
        return None

    def getIntersectionNode_two_pointers(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        pA, pB = headA, headB
        while pA and pB:
            if pA == pB:
                return pA
            pA = pA.next
            pB = pB.next
            if not pA and not pB:
                break
            if not pA:
                pA = headB
            if not pB:
                pB = headA
        return None

    def getIntersectionNode_two_pointers_short(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        if not headA or not headB:
            return None

        pA, pB = headA, headB

        while pA != pB:
            pA = pA.next if pA else headB
            pB = pB.next if pB else headA

        return pA  # Either the intersection node or None
