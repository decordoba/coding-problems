"""
Url: https://leetcode.com/explore/interview/card/top-interview-questions-easy/127/strings/887/
Title: Longest Common Prefix
Official difficulty: Easy
Real difficulty: 4/10

Description:
    Write a function to find the longest common prefix string amongst an array of strings.

    If there is no common prefix, return an empty string "".

Example 1:
    Input: strs = ["flower","flow","flight"]
    Output: "fl"

Example 2:
    Input: strs = ["dog","racecar","car"]
    Output: ""
    Explanation: There is no common prefix among the input strings.

Constraints:
    1 <= strs.length <= 200
    0 <= strs[i].length <= 200
    strs[i] consists of only lowercase English letters if it is non-empty.
"""
from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        elif len(strs) == 1:
            return strs[0]
        min_len = min([len(s) for s in strs])
        if min_len == 0:
            return ""
        for i in range(min_len):
            c = strs[0][i]
            for s in strs[1:]:
                if s[i] != c:
                    return s[:i]
        return strs[0][:min_len]

    def longestCommonPrefix_short_but_same(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        for i in range(len(strs[0])):
            c = strs[0][i]
            for s in strs[1:]:
                if i >= len(s) or s[i] != c:
                    return s[:i]
        return strs[0]
