"""
Url: https://leetcode.com/explore/interview/card/top-interview-questions-medium/103/array-and-strings/780/
Title: Longest Palindromic Substring
Official difficulty: Medium
Real difficulty: 5/10

Description:
    Given a string `s`, return the longest palindromic substring in `s`.

Example 1:
    Input: s = "babad"
    Output: "bab"
    Explanation: "aba" is also a valid answer.

Example 2:
    Input: s = "cbbd"
    Output: "bb"

Constraints:
    1 <= s.length <= 1000
    s consists of only digits and English letters.
"""


class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        pal = s[0] if n > 0 else s
        for i in range(1, n):
            prev1, prev2 = i - 1, i - 2
            for prev, len_pal in [(prev1, 0), (prev2, 1)]:
                le, ri = prev, i
                while le >= 0 and ri < n and s[le] == s[ri]:
                    len_pal += 2
                    le -= 1
                    ri += 1
                if len_pal > len(pal):
                    pal = s[le + 1:ri]
        return pal

    def longestPalindrome_same(self, s: str) -> str:
        def expand_around_center(left: int, right: int) -> str:
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1:right]

        longest = ""
        for i in range(len(s)):
            p1 = expand_around_center(i, i)
            p2 = expand_around_center(i, i + 1)
            if len(p1) > len(longest):
                longest = p1
            if len(p2) > len(longest):
                longest = p2
        return longest

    def longestPalindrome_best_but_too_hard(self, s: str) -> str:
        if not s:
            return ""

        # Preprocess the string
        T = "#".join(f"^{s}$")
        n = len(T)
        P = [0] * n
        C = R = 0

        for i in range(1, n - 1):
            mirror = 2 * C - i  # i' = C - (i - C)

            if i < R:
                P[i] = min(R - i, P[mirror])

            # Attempt to expand around center i
            while T[i + P[i] + 1] == T[i - P[i] - 1]:
                P[i] += 1

            # If palindrome centered at i expands past R, adjust center and right boundary
            if i + P[i] > R:
                C, R = i, i + P[i]

        # Find the maximum element in P
        max_len = max(P)
        center_index = P.index(max_len)
        start = (center_index - max_len) // 2  # Remove the '#' padding
        return s[start:start + max_len]
