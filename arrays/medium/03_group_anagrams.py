"""
Url: https://leetcode.com/explore/interview/card/top-interview-questions-medium/103/array-and-strings/778/
Title: Group Anagrams
Official difficulty: Medium
Real difficulty: 4/10

Description:
    Given an array of strings `strs`, group the anagrams together.
    You can return the answer in any order.

Example 1:
    Input: strs = ["eat","tea","tan","ate","nat","bat"]
    Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Example 2:
    Input: strs = [""]
    Output: [[""]]

Example 3:
    Input: strs = ["a"]
    Output: [["a"]]

Constraints:
    1 <= strs.length <= 10^4
    0 <= strs[i].length <= 100
    strs[i] consists of lowercase English letters.
"""


from collections import Counter, defaultdict
from typing import List

ORD_A = ord("a")


class Solution:
    def groupAnagrams_best(self, strs: List[str]) -> List[List[str]]:
        """O(n * k)."""
        r = []
        d = {}
        for s in strs:
            vals = [0] * 26
            for c in s:
                vals[ord(c) - ORD_A] += 1
            vals = tuple(vals)
            if vals in d:
                d[vals].append(s)
            else:
                el = [s]
                r.append(el)
                d[vals] = el
        return r

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """O(n * k * log(k))."""
        r = []
        d = {}
        for s in strs:
            ordered_s = "".join(sorted(s))
            if ordered_s in d:
                d[ordered_s].append(s)
            else:
                el = [s]
                r.append(el)
                d[ordered_s] = el
        return r

    def groupAnagrams_short_but_same(self, strs: List[str]) -> List[List[str]]:
        anagram_map = defaultdict(list)
        for s in strs:
            ordered_s = tuple(sorted(s))
            anagram_map[ordered_s].append(s)
        return list(anagram_map.values())

    def groupAnagrams2(self, strs: List[str]) -> List[List[str]]:
        """Attempt to increase efficiency but takes longer unless strings are very long"""
        r = []
        d = {}
        for s in strs:
            x = Counter(s)
            ordered_s = ""
            for c in sorted(x.keys()):
                ordered_s += c + str(x[c])
            if ordered_s in d:
                d[ordered_s].append(s)
            else:
                el = [s]
                r.append(el)
                d[ordered_s] = el
        return r
