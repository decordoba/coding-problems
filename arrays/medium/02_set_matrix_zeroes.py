"""
Url: https://leetcode.com/explore/interview/card/top-interview-questions-medium/103/array-and-strings/777/
Title: Set Matrix Zeroes
Official difficulty: Medium
Real difficulty: 6/10

Description:
    Given an m x n integer matrix `matrix`, if an element is 0, set its entire row and column to 0's.
    You must do it in place.

Example 1:
    Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
    Output: [[1,0,1],[0,0,0],[1,0,1]]

Example 2:
    Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
    Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]

Constraints:
    m == matrix.length
    n == matrix[0].length
    1 <= m, n <= 200
    -2^31 <= matrix[i][j] <= 2^31 - 1

Follow-up:
    A straightforward solution using O(mn) space is probably a bad idea.
    A simple improvement uses O(m + n) space, but still not the best solution.
    Could you devise a constant space solution?
"""


from typing import List


class Solution:
    def setZeroes1(self, matrix: List[List[int]]) -> None:
        """O(1) space. Use first row only to track 0s."""
        m = len(matrix)
        n = len(matrix[0])

        # determine if first row has 0
        first_row_has_zero = 0 in matrix[0]
        # mark columns with 0 in the first row
        for i in range(1, m):
            for j in range(n):
                if matrix[i][j] == 0:
                    matrix[0][j] = 0
        # set rows with 0 to 0
        for i in range(1, m):
            if 0 in matrix[i]:
                for j in range(n):
                    matrix[i][j] = 0
        # set columns with 0 to 0
        for j in range(n):
            if matrix[0][j] == 0:
                for i in range(m):
                    matrix[i][j] = 0
        # set first row to 0 if it had a 0
        if first_row_has_zero:
            for j in range(n):
                matrix[0][j] = 0

    def setZeroes2(self, matrix: List[List[int]]) -> None:
        """O(1) space. Use first col and row to track 0s."""
        m = len(matrix)
        n = len(matrix[0])

        # determine if first row has 0
        first_row_has_zero = 0 in matrix[0]
        first_col_has_zero = 0 in [row[0] for row in matrix]
        # mark columns with 0 in the first row
        for i in range(1, m):
            for j in range(n):
                if matrix[i][j] == 0:
                    matrix[0][j] = 0
                    matrix[i][0] = 0
        # set cells with 0 row or col to 0
        for i in range(1, m):
            for j in range(1, n):
                if matrix[0][j] == 0 or matrix[i][0] == 0:
                    matrix[i][j] = 0
        # set first row to 0 if it had a 0
        if first_row_has_zero:
            for j in range(n):
                matrix[0][j] = 0
        # set first col to 0 if it had a 0
        if first_col_has_zero:
            for i in range(m):
                matrix[i][0] = 0

    def setZeroes_m_plus_n_space(self, matrix: List[List[int]]) -> None:
        """O(m+n) space."""
        m = len(matrix)
        n = len(matrix[0])

        horiz = [False] * m
        vert = [False] * n

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    horiz[i] = True
                    vert[j] = True
        for i in range(m):
            for j in range(n):
                if horiz[i] or vert[j]:
                    matrix[i][j] = 0
