"""
Url: https://leetcode.com/explore/interview/card/top-interview-questions-easy/97/dynamic-programming/569/
Title: Climbing Stairs
Official difficulty: Easy
Real difficulty: 5/10

Description:
    You are climbing a staircase. It takes n steps to reach the top.

    Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb
    to the top?

Example 1:
    Input: n = 2
    Output: 2
    Explanation: There are two ways to climb to the top.
        1. 1 step + 1 step
        2. 2 steps

Example 2:
    Input: n = 3
    Output: 3
    Explanation: There are three ways to climb to the top.
        1. 1 step + 1 step + 1 step
        2. 1 step + 2 steps
        3. 2 steps + 1 step

Constraints:
    1 <= n <= 45
"""


class Solution:
    def climbStairs(self, n: int) -> int:
        steps_allowed = [1, 2]
        dp = [0] * (n + 1)
        dp[0] = 1
        for i in range(1, n + 1):
            for s in steps_allowed:
                prev = i - s
                if prev < 0:
                    continue
                dp[i] += dp[prev]
        return dp[n]

    def climbStairs_fibonacci(self, n: int) -> int:
        """O(1) space."""
        # we only ever need the last 2 numbers, so we can do fibonacci
        if n <= 2:
            return n
        a, b = 1, 2
        for _ in range(3, n + 1):
            a, b = b, a + b
        return b

    def climbStairs_choosing_steps(self, n: int, steps_allowed: list[int]) -> int:
        """With variable for steps."""
        dp = [0] * (n + 1)
        dp[0] = 1

        for i in range(1, n + 1):
            for step in steps_allowed:
                if i - step >= 0:
                    dp[i] += dp[i - step]

        return dp[n]
