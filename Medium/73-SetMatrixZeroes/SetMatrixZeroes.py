from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows, cols = len(matrix), len(matrix[0])
        zerows, zecols = set(), set()

        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == 0:
                    zerows.add(r)
                    zecols.add(c)

        for row in zerows:
            for c in range(cols):
                matrix[row][c] = 0

        for col in zecols:
            for r in range(rows):
                matrix[r][col] = 0


    # O(1) Space.
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows, cols = len(matrix), len(matrix[0])
        firstRowHasZero, firstColHasZero = False, False
        
        for row in range(rows):
            for col in range(cols):
                if matrix[row][col] == 0:
                    if row == 0:
                        firstRowHasZero = True
                    if col == 0:
                        firstColHasZero = True
                    matrix[0][col] = 0
                    matrix[row][0] = 0

        for row in range(1, rows):
            for col in range(1, cols):
                if matrix[row][0] == 0 or matrix[0][col] == 0:
                    matrix[row][col] = 0

        if firstRowHasZero:
            for col in range(cols):
                matrix[0][col] = 0
        if firstColHasZero:
            for row in range(rows):
                matrix[row][0] = 0