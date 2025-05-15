"""
Url: https://leetcode.com/explore/interview/card/top-interview-questions-easy/102/math/745/
Title: Power of Three
Official difficulty: Easy
Real difficulty: 5/10

Description:
    Given an integer n, return true if it is a power of three. Otherwise, return false.

    An integer n is a power of three if there exists an integer x such that n == 3^x.

Example 1:
    Input: n = 27
    Output: true
    Explanation: 27 = 3^3

Example 2:
    Input: n = 0
    Output: false
    Explanation: There is no x where 3^x = 0.

Example 3:
    Input: n = -1
    Output: false
    Explanation: There is no x where 3^x = -1.

Constraints:
    -2^31 <= n <= 2^31 - 1

Follow-up:
    Could you solve it without loops or recursion?
"""


import math


class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n < 1:
            return False
        while n > 1:
            if n % 3 != 0:
                return False
            n = n // 3
        return True

    def isPowerOfThree_better(self, n: int) -> bool:
        if n < 1:
            return False
        while n % 3 != 0:
            n = n // 3
        return n == 1

    def isPowerOfThree_no_loops(self, n: int) -> bool:
        """Assuming 1162261467 is the largest int that can exist."""
        return n > 0 and 1162261467 % n == 0

    def isPowerOfThree_no_loops2(self, n: int) -> bool:
        """May have floating point problems."""
        if n <= 0:
            return False
        x = math.log10(n) / math.log10(3)
        return x.is_integer()
