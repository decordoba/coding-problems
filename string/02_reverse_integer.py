"""
Url: https://leetcode.com/explore/interview/card/top-interview-questions-easy/127/strings/880/
Title: Reverse Integer
Official difficulty: Easy
Real difficulty: 6/10

Description:
    Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes
    the value to go outside the signed 32-bit integer range [-2^31, 2^31 - 1], then return 0.

    Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

Example 1:
    Input: x = 123
    Output: 321

Example 2:
    Input: x = -123
    Output: -321

Example 3:
    Input: x = 120
    Output: 21

Constraints:
    -2^31 <= x <= 2^31 - 1
"""


class Solution:
    def reverse_string(self, x: int) -> int:

        def s1_gt_s2(s1: str, s2: str):
            """Only for positive numbers without leading 0s."""
            if len(s1) != len(s2):
                return len(s1) > len(s2)
            for c1, c2 in zip(s1, s2):
                if c1 > c2:
                    return True
                elif c1 < c2:
                    return False
            return False  # numbers are the same

        min_int = -2 ** 31
        max_int = ((2 ** 30) - 1) * 2 + 1  # (2 ** 31) - 1
        neg = True if x < 0 else False
        s = str(x)  # transform to str to avoid 64-bit int
        s = s[1:] if neg else s  # remove sign
        s = s[::-1]  # reverse
        if neg:
            return int("-" + s) if not s1_gt_s2(s, str(min_int)[1:]) else 0
        else:
            return int(s) if not s1_gt_s2(s, str(max_int)) else 0

    def reverse_numbers(self, x: int) -> int:
        # prevent ever having 2 ** 31 = -2 ** 31 * -1
        if x == -2 ** 31:
            return 0
        tmp = 214748364  # 2 ** 31 // 10
        factor = -1 if x < 0 else 1
        x = x * factor
        rev = 0
        # get close to number, but stay 10 away
        while x > 0:
            digit = x % 10
            x = x // 10
            if rev > tmp or (rev == tmp and digit > 7):  # 1st digit > 7, last num of -2 ** 31 * -1
                return 0
            rev = rev * 10 + digit
        return rev * factor
