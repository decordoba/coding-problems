"""
Url: https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/770/
Title: Rotate Image
Official difficulty: Easy
Real difficulty: 7/10

Description:
    You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

    You have to rotate the image in-place, which means you have to modify the input 2D matrix directly.
    DO NOT allocate another 2D matrix and do the rotation.

Example 1:
    Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
    Output: [[7,4,1],[8,5,2],[9,6,3]]

Example 2:
    Input: matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
    Output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]

Constraints:
    n == matrix.length == matrix[i].length
    1 <= n <= 20
    -1000 <= matrix[i][j] <= 1000
"""

from typing import List


class Solution:
    def rotate_normal(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        N = len(matrix)
        n = N - 1
        for y in range(N // 2):
            for x in range(y, N - 1 - y):
                m1 = matrix[y][x]
                m2 = matrix[x][n - y]
                m3 = matrix[n - y][n - x]
                m4 = matrix[n - x][y]
                matrix[y][x] = m4
                matrix[x][n - y] = m1
                matrix[n - y][n - x] = m2
                matrix[n - x][y] = m3

    def rotate_transpose_invert_weird(self, matrix: List[List[int]]) -> None:
        """Transpose and rotate."""

        def transpose(matrix, N):
            for x in range(N - 1):
                for y in range(N - x - 1):
                    y2, x2 = N - x - 1, N - y - 1
                    matrix[x][y], matrix[x2][y2] = matrix[x2][y2], matrix[x][y]

        def invert(matrix, N):
            for y in range(N//2):
                for x in range(N):
                    matrix[y][x], matrix[N - y - 1][x] = matrix[N - y - 1][x], matrix[y][x]

        N = len(matrix)
        transpose(matrix, N)
        invert(matrix, N)

    def rotate_transpose_invert_normal(self, matrix):
        n = len(matrix)
        # transpose
        for i in range(n):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        # reverse each row
        for row in matrix:
            row.reverse()


"""
Normal Method
    Problem
    1 2 3 4
    5 6 7 8
    9 A B C
    D E F G
    Transpose
    1 5 9 D
    2 6 A E
    3 7 B F
    4 8 C G
    Reverse rows
    D 9 5 1
    E A 6 2
    F B 7 3
    G C 8 4

Weird Method
    Problem
    1 2 3 4
    5 6 7 8
    9 A B C
    D E F G
    Transpose in other diagonal
    G C 8 4
    F B 7 3
    E A 6 2
    D 9 5 1
    Reverse columns
    D 9 5 1
    E A 6 2
    F B 7 3
    G C 8 4
"""
