"""
Url: https://leetcode.com/explore/interview/card/top-interview-questions-easy/127/strings/882/
Title: Valid Anagram
Official difficulty: Easy
Real difficulty: 3/10

Description:
    Given two strings s and t, return true if t is an anagram of s, and false otherwise.

Example 1:
    Input: s = "anagram", t = "nagaram"
    Output: true

Example 2:
    Input: s = "rat", t = "car"
    Output: false

Constraints:
    1 <= s.length, t.length <= 5 * 10^4
    s and t consist of lowercase English letters.

Follow-up:
    What if the inputs contain Unicode characters?
    How would you adapt your solution to such a case?
"""


class Solution:
    def isAnagram_counter(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        sc, tc = {}, {}
        for c in s:
            if c in sc:
                sc[c] += 1
            else:
                sc[c] = 1
        for c in t:
            if c in tc:
                tc[c] += 1
            else:
                tc[c] = 1
        return sc == tc

    def isAnagram_list(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        sc, tc = [0] * 26, [0] * 26
        for c in s:
            sc[ord(c) - ord("a")] += 1
        for c in t:
            tc[ord(c) - ord("a")] += 1
        return sc == tc

    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        counts = [0] * 26
        for c1, c2 in zip(s, t):
            counts[ord(c1) - ord("a")] += 1
            counts[ord(c2) - ord("a")] -= 1
        return all(count == 0 for count in counts)
