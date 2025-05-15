"""
Url: https://leetcode.com/explore/interview/card/top-interview-questions-easy/102/math/878/
Title: Roman to Integer
Official difficulty: Easy
Real difficulty: 4/10

Description:
    Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

    Symbol       Value
    I             1
    V             5
    X             10
    L             50
    C             100
    D             500
    M             1000

    For example, 2 is written as II in Roman numeral, just two ones added together.
    12 is written as XII, which is X + II.
    The number 27 is written as XXVII, which is XX + V + II.

    Roman numerals are usually written largest to smallest from left to right.
    However, the numeral for four is not IIII. Instead, it is IV. Because the one is before
    the five we subtract it making four. The same principle applies to the number nine (IX).

    There are six instances where subtraction is used:
    * I can be placed before V (5) and X (10) to make 4 and 9.
    * X can be placed before L (50) and C (100) to make 40 and 90.
    * C can be placed before D (500) and M (1000) to make 400 and 900.

    Given a Roman numeral, convert it to an integer.

Example 1:
    Input: s = "III"
    Output: 3
    Explanation: III = 3

Example 2:
    Input: s = "LVIII"
    Output: 58
    Explanation: L = 50, V = 5, III = 3

Example 3:
    Input: s = "MCMXCIV"
    Output: 1994
    Explanation: M = 1000, CM = 900, XC = 90, IV = 4

Constraints:
    1 <= s.length <= 15
    s contains only the characters ('I', 'V', 'X', 'L', 'C', 'D', 'M').
    It is guaranteed that s is a valid Roman numeral in the range [1, 3999].
"""


class Solution:
    def romanToInt(s: str) -> int:
        s = s.upper()
        n = 0
        prev_i = 0
        prev_x = 0
        prev_c = 0
        for c in s:
            add_prevs = True
            if c == "I":
                prev_i += 1
                add_prevs = False
            elif c == "V":
                if prev_i > 0:
                    prev_i = 0
                    n += 4
                else:
                    n += 5
            elif c == "X":
                if prev_i > 0:
                    prev_i = 0
                    n += 9
                else:
                    prev_x += 1
                    add_prevs = False
            elif c == "L":
                if prev_x > 0:
                    prev_x = 0
                    n += 40
                else:
                    n += 50
            elif c == "C":
                if prev_x > 0:
                    prev_x = 0
                    n += 90
                else:
                    prev_c += 1
                    add_prevs = False
            elif c == "D":
                if prev_c > 0:
                    prev_c = 0
                    n += 400
                else:
                    n += 500
            elif c == "M":
                if prev_c > 0:
                    prev_c = 0
                    n += 900
                else:
                    n += 1000
            else:
                raise ValueError(f"Unknown character {c}")
            if add_prevs:
                n += prev_i + 10 * prev_x + 100 * prev_c
                prev_i = prev_x = prev_c = 0
        n += prev_i + 10 * prev_x + 100 * prev_c
        return n

    def romanToInt_short(self, s: str) -> int:
        roman = {
            "I": 1, "V": 5, "X": 10, "L": 50,
            "C": 100, "D": 500, "M": 1000
        }

        total = 0
        prev = 0

        for char in reversed(s):
            value = roman[char]
            if value < prev:
                total -= value
            else:
                total += value
            prev = value

        return total
