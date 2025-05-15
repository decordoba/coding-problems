"""
Url: https://leetcode.com/explore/interview/card/top-interview-questions-easy/127/strings/884/
Title: String to Integer (atoi)
Official difficulty: Easy
Real difficulty: 7/10

Description:
    Implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer.

    The algorithm for myAtoi(string s) is as follows:

    1. Whitespace: Ignore any leading whitespace (" ").
    2. Signedness: Determine the sign by checking if the next character is '-' or '+',
       assuming positivity if neither is present.
    3. Conversion: Read the integer by skipping leading zeros until a non-digit character
       is encountered or the end of the string is reached. If no digits were read, then the result is 0.
    4. Rounding: If the integer is out of the 32-bit signed integer range [-2^31, 2^31 - 1],
       then round the integer to remain in the range. Specifically:
       - Integers less than -2^31 should be rounded to -2^31.
       - Integers greater than 2^31 - 1 should be rounded to 2^31 - 1.
    5. Return the integer as the final result.

Example 1:
    Input: s = "42"
    Output: 42
    Explanation:
        The characters "42" are read directly as the integer 42.

Example 2:
    Input: s = "   -042"
    Output: -42
    Explanation:
        Leading whitespace is ignored, '-' sign is detected, and "042" is read as 42.

Example 3:
    Input: s = "1337c0d3"
    Output: 1337
    Explanation:
        Reading stops at the non-digit character 'c'.

Example 4:
    Input: s = "0-1"
    Output: 0
    Explanation:
        Reading stops after reading "0" since '-' is not part of a valid number continuation.

Example 5:
    Input: s = "words and 987"
    Output: 0
    Explanation:
        Reading stops immediately at the non-digit character 'w'.

Constraints:
    0 <= s.length <= 200
    s consists of English letters (lower-case and upper-case), digits (0-9), ' ', '+', '-', and '.'.
"""


class Solution:
    def myAtoi(self, s: str) -> int:
        # remove spaces
        s = s.strip()
        # handle empty strings
        if len(s) == 0:
            return 0
        # handle +/-
        factor = 1
        i = 0
        if s[i] == "-":
            i += 1
            factor = -1
        elif s[i] == "+":
            i += 1
        # handle digit and max comparisons
        n = 0
        min_int = -2 ** 31
        max_int = 2 ** 31 - 1  # this is technically not ok, as we pass 2**31 - 1
        prev_to_max = max_int // 10
        max_last_digit = str(max_int)[-1]
        min_last_digit = str(min_int)[-1]
        for c in s[i:]:
            if not c.isdigit():
                break
            if (factor > 0) and (n > prev_to_max or (n == prev_to_max and c > max_last_digit)):
                return max_int
            elif (factor < 0) and (n > prev_to_max or (n == prev_to_max and c > min_last_digit)):
                return min_int
            n = n * 10 + int(c)
        return n * factor
