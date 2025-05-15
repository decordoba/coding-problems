"""
Url: https://leetcode.com/explore/interview/card/top-interview-questions-easy/102/math/744/
Title: Count Primes
Official difficulty: Easy
Real difficulty: 6/10

Description:
    Given an integer n, return the number of prime numbers that are strictly less than n.

Example 1:
    Input: n = 10
    Output: 4
    Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, and 7.

Example 2:
    Input: n = 0
    Output: 0

Example 3:
    Input: n = 1
    Output: 0

Constraints:
    0 <= n <= 5 * 10^6
"""


class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 2:
            return 0
        is_prime = [True] * n
        is_prime[0] = is_prime[1] = False
        primes = 0
        for i in range(2, n):
            if is_prime[i]:
                primes += 1
                c = i * i
                while c < n:
                    is_prime[c] = False
                    c += i
        return primes
