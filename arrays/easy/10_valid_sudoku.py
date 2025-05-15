"""
Url: https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/769/
Title: Valid Sudoku
Official difficulty: Easy
Real difficulty: 7/10

Description:
    Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated
    according to the following rules:

    * Each row must contain the digits 1-9 without repetition.
    * Each column must contain the digits 1-9 without repetition.
    * Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.

    Note:
    A Sudoku board (partially filled) could be valid but is not necessarily solvable.
    Only the filled cells need to be validated according to the mentioned rules.

Example 1:
    Input: board =
        [["5","3",".",".","7",".",".",".","."],
         ["6",".",".","1","9","5",".",".","."],
         [".","9","8",".",".",".",".","6","."],
         ["8",".",".",".","6",".",".",".","3"],
         ["4",".",".","8",".","3",".",".","1"],
         ["7",".",".",".","2",".",".",".","6"],
         [".","6",".",".",".",".","2","8","."],
         [".",".",".","4","1","9",".",".","5"],
         [".",".",".",".","8",".",".","7","9"]]
    Output: true

Example 2:
    Input: board =
        [["8","3",".",".","7",".",".",".","."],
         ["6",".",".","1","9","5",".",".","."],
         [".","9","8",".",".",".",".","6","."],
         ["8",".",".",".","6",".",".",".","3"],
         ["4",".",".","8",".","3",".",".","1"],
         ["7",".",".",".","2",".",".",".","6"],
         [".","6",".",".",".",".","2","8","."],
         [".",".",".","4","1","9",".",".","5"],
         [".",".",".",".","8",".",".","7","9"]]
    Output: false
    Explanation: Same as Example 1, except with the 5 in the top left corner being modified to 8.
        Since there are two 8's in the top left 3x3 sub-box, it is invalid.

Constraints:
    board.length == 9
    board[i].length == 9
    board[i][j] is a digit 1-9 or '.'.
"""

from typing import List


class Solution:
    def isValidSudoku_validation_original(self, board: List[List[str]]) -> bool:

        def group_valid(g):
            c = 0
            s = set()
            for n in g:
                if n != ".":
                    c += 1
                    s.add(n)
            return c == len(s)

        # Add lines
        validations = [line for line in board]
        # Add columns
        for i in range(9):
            col = [line[i] for line in board]
            validations.append(col)
        # Add group
        for x in range(0, 9, 3):
            for y in range(0, 9, 3):
                group = [board[i + x][j + y] for i in range(3) for j in range(3)]
                validations.append(group)
        # Validate all groups
        for line in validations:
            if not group_valid(line):
                return False
        return True

    def isValidSudoku_validation_short(self, board: List[List[str]]) -> bool:
        rows = [line for line in board]
        cols = [[line[i] for line in board] for i in range(9)]
        boxes = [[board[i + x][j + y] for i in range(3) for j in range(3)] for x in range(0, 9, 3) for y in range(0, 9, 3)]

        for line in rows + cols + boxes:
            s = set()
            for n in line:
                if n != ".":
                    if n in s:
                        return False
                    s.add(n)
        return True

    def isValidSudoku_sets(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        for y in range(9):
            for x in range(9):
                n = board[y][x]

                if n == ".":
                    continue

                box_idx = y // 3 + 3 * (x // 3)
                if n in rows[y] or n in cols[x] or n in boxes[box_idx]:
                    return False
                rows[y].add(n)
                cols[x].add(n)
                boxes[box_idx].add(n)
        return True
