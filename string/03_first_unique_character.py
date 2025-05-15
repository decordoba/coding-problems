"""
Url: https://leetcode.com/explore/interview/card/top-interview-questions-easy/127/strings/881/
Title: First Unique Character in a String
Official difficulty: Easy
Real difficulty: 4/10

Description:
    Given a string s, find the first non-repeating character in it and return its index.
    If it does not exist, return -1.

Example 1:
    Input: s = "leetcode"
    Output: 0
    Explanation: The character 'l' at index 0 is the first character that does not occur at any other index.

Example 2:
    Input: s = "loveleetcode"
    Output: 2

Example 3:
    Input: s = "aabb"
    Output: -1

Constraints:
    1 <= s.length <= 10^5
    s consists of only lowercase English letters.
"""

from collections import Counter


class Solution:
    def firstUniqChar(self, s: str) -> int:
        ht = {}
        for i, c in enumerate(s):
            if c not in ht:
                ht[c] = i
            else:
                ht[c] = None
        min_i = len(s)
        for c, i in ht.items():
            if i is not None:
                min_i = min(i, min_i)
        return min_i if min_i < len(s) else -1

    def firstUniqChar_two_pass(self, s: str) -> int:
        ht = Counter(s)
        for c, i in s:
            if ht[c] == 1:
                return i
        return -1
