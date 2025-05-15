"""
Url: https://leetcode.com/explore/interview/card/top-interview-questions-easy/127/strings/883/
Title: Valid Palindrome
Official difficulty: Easy
Real difficulty: 4/10

Description:
    A phrase is a palindrome if, after converting all uppercase letters into lowercase letters
    and removing all non-alphanumeric characters, it reads the same forward and backward.
    Alphanumeric characters include letters and numbers.

    Given a string s, return true if it is a palindrome, or false otherwise.

Example 1:
    Input: s = "A man, a plan, a canal: Panama"
    Output: true
    Explanation: "amanaplanacanalpanama" is a palindrome.

Example 2:
    Input: s = "race a car"
    Output: false
    Explanation: "raceacar" is not a palindrome.

Example 3:
    Input: s = " "
    Output: true
    Explanation: s is an empty string "" after removing non-alphanumeric characters.
        Since an empty string reads the same forward and backward, it is a palindrome.

Constraints:
    1 <= s.length <= 2 * 10^5
    s consists only of printable ASCII characters.
"""


class Solution:
    def isPalindrome_directly(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        while l < r:
            cl, cr = s[l], s[r]
            if not cl.isalnum():
                l += 1
            elif not cr.isalnum():
                r -= 1
            elif cl.lower() != cr.lower():
                return False
            else:
                l += 1
                r -= 1
        return True

    def isPalindrome_filter_first(self, s: str) -> bool:
        s = "".join(c.lower() for c in s if c.isalnum())
        l, r = 0, len(s) - 1
        while l < r:
            if s[l] != s[r]:
                return False
            else:
                l += 1
                r -= 1
        return True

    def isPalindrome_nested_loops(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        while l < r:
            cl, cr = s[l], s[r]
            while l < r and not cl.isalnum():
                l += 1
            while l < r and not cr.isalnum():
                r -= 1
            if cl.lower() != cr.lower():
                return False
            l += 1
            r -= 1
        return True
