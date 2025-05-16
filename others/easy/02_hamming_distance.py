"""
Url: https://leetcode.com/explore/interview/card/top-interview-questions-easy/99/others/762/
Title: Hamming Distance
Official difficulty: Easy
Real difficulty: 4/10

Description:
    The Hamming distance between two integers is the number of positions at which the
    corresponding bits are different.

    Given two integers x and y, return the Hamming distance between them.

Example 1:
    Input: x = 1, y = 4
    Output: 2
    Explanation:
        1   (0 0 0 1)
        4   (0 1 0 0)
             ↑   ↑
        The arrows point to positions where the corresponding bits are different.

Example 2:
    Input: x = 3, y = 1
    Output: 1

Constraints:
    0 <= x, y <= 2^31 - 1

Note:
    This question is the same as Leetcode 2220: Minimum Bit Flips to Convert Number.
"""


class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        d = 0
        while x > 0 or y > 0:
            if x % 2 != y % 2:
                d += 1
            x //= 2
            y //= 2
        return d

    def hammingDistance_bin(self, x: int, y: int) -> int:
        return bin(x ^ y).count("1")

    def hammingDistance_bin_count(self, x: int, y: int) -> int:
        xor = x ^ y
        count = 0
        while xor:
            xor &= xor - 1
            count += 1
        return count
