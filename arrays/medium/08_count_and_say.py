"""
Url: https://leetcode.com/explore/interview/card/top-interview-questions-medium/103/array-and-strings/782/
Title: Count and Say
Official difficulty: Medium
Real difficulty: 4/10

Description:
    The count-and-say sequence is a sequence of digit strings defined by the recursive formula:

    countAndSay(1) = "1"
    countAndSay(n) is the run-length encoding of countAndSay(n - 1).

    Run-length encoding (RLE) is a string compression method that works by replacing consecutive
    identical characters (repeated 2 or more times) with the concatenation of the character and
    the number marking the count of the characters (length of the run). For example, to compress
    the string "3322251" we replace "33" with "23", replace "222" with "32", replace "5" with "15"
    and replace "1" with "11". Thus the compressed string becomes "23321511".

    Given a positive integer `n`, return the nth element of the count-and-say sequence.

Example 1:
    Input: n = 4
    Output: "1211"
    Explanation:
        countAndSay(1) = "1"
        countAndSay(2) = RLE of "1" = "11"
        countAndSay(3) = RLE of "11" = "21"
        countAndSay(4) = RLE of "21" = "1211"

Example 2:
    Input: n = 1
    Output: "1"
    Explanation:
        This is the base case.

Constraints:
    1 <= n <= 30

Follow-up:
    Could you solve it iteratively?
"""


class Solution:
    def countAndSay(self, n: int) -> str:
        s = "1"
        for _ in range(1, n):
            prev = None
            count = 0
            new_s = ""
            for c in s:
                if c == prev:
                    count += 1
                else:
                    if count > 0:
                        new_s += f"{count}{prev}"
                    prev = c
                    count = 1
            new_s += f"{count}{prev}"
            s = new_s
        return s

    def countAndSay_with_list(self, n: int) -> str:
        """More efficient, string concatenation creates a new str."""
        s = "1"
        for _ in range(1, n):
            prev = None
            count = 0
            new_s = []
            for c in s:
                if c == prev:
                    count += 1
                else:
                    if prev is not None:
                        new_s .append(f"{count}{prev}")
                    prev = c
                    count = 1
            new_s.append(f"{count}{prev}")
            s = "".join(new_s)
        return s
