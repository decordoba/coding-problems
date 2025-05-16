"""
Url: https://leetcode.com/explore/interview/card/top-interview-questions-easy/99/others/762/
Title: Pascal's Triangle
Official difficulty: Easy
Real difficulty: 3/10

Description:
    Given an integer numRows, return the first numRows of Pascal's triangle.

    In Pascal's triangle, each number is the sum of the two numbers directly above it.

Example 1:
    Input: numRows = 5
    Output: [[1],
             [1,1],
             [1,2,1],
             [1,3,3,1],
             [1,4,6,4,1]]

Example 2:
    Input: numRows = 1
    Output: [[1]]

Constraints:
    1 <= numRows <= 30
"""


from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0:
            return []
        r = [[1]]
        for i in range(1, numRows):
            prev = r[i - 1]
            nxt = []
            for j in range(i):
                if j == 0:
                    nxt.append(prev[0])
                else:
                    nxt.append(prev[j] + prev[j - 1])
            nxt.append(prev[-1])
            r.append(nxt)
        return r

    def generate_short(self, numRows: int) -> list[list[int]]:
        triangle = []

        for i in range(numRows):
            row = [1] * (i + 1)
            for j in range(1, i):
                row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
            triangle.append(row)

        return triangle
