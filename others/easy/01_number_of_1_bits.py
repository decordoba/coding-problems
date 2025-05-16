"""
Url: https://leetcode.com/explore/interview/card/top-interview-questions-easy/99/others/565/
Title: Number of 1 Bits
Official difficulty: Easy
Real difficulty: 4/10

Description:
    Given a positive integer n, write a function that returns the number of set bits
    in its binary representation (also known as the Hamming weight).

Example 1:
    Input: n = 11
    Output: 3
    Explanation: The input binary string 1011 has a total of three set bits.

Example 2:
    Input: n = 128
    Output: 1
    Explanation: The input binary string 10000000 has a total of one set bit.

Example 3:
    Input: n = 2147483645
    Output: 30
    Explanation: The input binary string 1111111111111111111111111111101 has a total
                 of thirty set bits.

Constraints:
    1 <= n <= 2^31 - 1

Follow-up:
    If this function is called many times, how would you optimize it?
"""


class Solution:
    def hammingWeight(self, n: int) -> int:
        """O(logn), where n is n, and logn is number of bits."""
        # get base2 to be over n
        base2 = 1
        while base2 < n:
            base2 *= 2

        # subtract bits of n and count how many
        r = 0
        while n > 0:
            while base2 > n:
                base2 //= 2
            n -= base2
            r += 1

        return r

    def hammingWeight_best(self, n: int) -> int:
        """O(k), where k is number of bits to 1."""
        count = 0
        while n:
            n &= n - 1  # clears the lowest set bit
            count += 1
        return count
