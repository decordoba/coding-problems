"""
Url: https://leetcode.com/explore/interview/card/top-interview-questions-medium/103/array-and-strings/779/
Title: Longest Substring Without Repeating Characters
Official difficulty: Medium
Real difficulty: 5/10

Description:
    Given a string `s`, find the length of the longest substring without duplicate characters.

Example 1:
    Input: s = "abcabcbb"
    Output: 3
    Explanation: The answer is "abc", with the length of 3.

Example 2:
    Input: s = "bbbbb"
    Output: 1
    Explanation: The answer is "b", with the length of 1.

Example 3:
    Input: s = "pwwkew"
    Output: 3
    Explanation: The answer is "wke", with the length of 3.
                 Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

Constraints:
    0 <= s.length <= 5 * 10^4
    s consists of English letters, digits, symbols and spaces.
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """Track with prev_rep last time a char was repeated."""
        last_pos = {}
        prev_rep = 0
        longest = 0
        for i, c in enumerate(s):
            if c in last_pos:
                longest = max(longest, i - prev_rep)
                prev_rep = max(prev_rep, last_pos[c] + 1)
            last_pos[c] = i
        longest = max(longest, len(s) - prev_rep)
        return longest

    def lengthOfLongestSubstring_same(self, s: str) -> int:
        char_idx = {}
        left = 0
        max_len = 0
        for right, c in enumerate(s):
            if c in char_idx and char_idx[c] >= left:
                left = char_idx[c] + 1
            char_idx[c] = right
            max_len = max(max_len, right - left + 1)
        return max_len
