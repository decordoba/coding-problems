"""
Url: https://leetcode.com/explore/interview/card/top-interview-questions-easy/127/strings/885/
Title: Implement strStr()
Official difficulty: Easy
Real difficulty: 8/10 (if using LPS)

Description:
    Given two strings needle and haystack, return the index of the first occurrence of needle
    in haystack, or -1 if needle is not part of haystack.

Example 1:
    Input: haystack = "sadbutsad", needle = "sad"
    Output: 0
    Explanation: "sad" occurs at index 0 and 6. The first occurrence is at index 0.

Example 2:
    Input: haystack = "leetcode", needle = "leeto"
    Output: -1
    Explanation: "leeto" did not occur in "leetcode", so we return -1.

Constraints:
    1 <= haystack.length, needle.length <= 10^4
    haystack and needle consist of only lowercase English characters.
"""


class Solution:
    def strStr_manual(self, haystack: str, needle: str) -> int:
        if len(needle) > len(haystack) or len(haystack) == 0 or len(needle) == 0:
            return -1
        for i in range(len(haystack) - len(needle) + 1):
            if needle[0] == haystack[i]:
                ni, hi = 1, i + 1
                match = True
                while ni < len(needle):
                    if needle[ni] != haystack[hi]:
                        match = False
                        break
                    ni += 1
                    hi += 1
                if match:
                    return i
        return -1

    def strStr_fast(self, haystack: str, needle: str) -> int:
        n = len(needle)
        m = len(haystack)
        if n == 0:
            return -1
        for i in range(m - n + 1):
            if needle[0] == haystack[i] and haystack[i:i + n] == needle:
                return i
        return -1

    def strStr_lps(haystack: str, needle: str) -> int:
        if len(needle) == 0:
            return -1

        def build_lps(pattern: str) -> list[int]:
            """Examples: aababaaab -> 010101223, ababacababababac -> 0012301234545456."""
            lps = [0] * len(pattern)
            length = 0  # length of the previous longest prefix suffix
            i = 1

            while i < len(pattern):
                if pattern[i] == pattern[length]:
                    length += 1
                    lps[i] = length
                    i += 1
                else:
                    if length != 0:
                        length = lps[length - 1]  # fallback
                    else:
                        lps[i] = 0
                        i += 1
            return lps

        # build lps O(n)
        lps = build_lps(needle)
        i = j = 0  # i for haystack, j for needle

        # search with lps O(m)
        while i < len(haystack):
            if haystack[i] == needle[j]:
                i += 1
                j += 1
                if j == len(needle):
                    return i - j
            else:
                if j != 0:
                    j = lps[j - 1]
                else:
                    i += 1

        return -1
