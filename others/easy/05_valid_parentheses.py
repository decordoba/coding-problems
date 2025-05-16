"""
Url: https://leetcode.com/explore/interview/card/top-interview-questions-easy/99/others/648/
Title: Valid Parentheses
Official difficulty: Easy
Real difficulty: 3/10

Description:
    Given a string s containing just the characters '(', ')', '{', '}', '[' and ']',
    determine if the input string is valid.

    An input string is valid if:
    * Open brackets must be closed by the same type of brackets.
    * Open brackets must be closed in the correct order.
    * Every close bracket has a corresponding open bracket of the same type.

Example 1:
    Input: s = "()"
    Output: true

Example 2:
    Input: s = "()[]{}"
    Output: true

Example 3:
    Input: s = "(]"
    Output: false

Example 4:
    Input: s = "([])"
    Output: true

Constraints:
    1 <= s.length <= 10^4
    s consists of parentheses only '()[]{}'.
"""


class Solution:
    def isValid_limited(self, s: str) -> bool:
        """Allows {(})."""
        closers = {
            ")": "(",
            "}": "{",
            "]": "[",
        }
        openers = {
            "(": 0,
            "{": 0,
            "[": 0,
        }
        for c in s:
            if c in openers:
                openers[c] += 1
            elif c in closers:
                opener_c = closers[c]
                openers[opener_c] -= 1
                if openers[opener_c] < 0:
                    return False
            else:
                raise ValueError(f"Character {c} not recognized")
        return sum([x for x in openers.values()]) == 0

    def isValid(self, s: str) -> bool:
        stack = []
        openers = set(["(", "{", "["])
        closers = {
            ")": "(",
            "}": "{",
            "]": "[",
        }
        for c in s:
            if c in openers:
                stack.append(c)
            elif c in closers:
                opener_c = closers[c]
                if len(stack) == 0 or stack[-1] != opener_c:
                    return False
                stack.pop()
            else:
                raise ValueError(f"Character {c} not recognized")
        return len(stack) == 0

    def isValid_short(self, s: str) -> bool:
        stack = []
        mapping = {")": "(", "]": "[", "}": "{"}

        for char in s:
            if char in mapping:
                top = stack.pop() if stack else "#"
                if mapping[char] != top:
                    return False
            else:
                stack.append(char)

        return not stack
