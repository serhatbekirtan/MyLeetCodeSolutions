from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        rows, cols = len(matrix), len(matrix[0])
        r, c, row, col = 0, 0, rows - 1, cols - 1
        res = [matrix[r][c]]
        flag = False

        def move(steps: int, dr: int, dc: int):
            nonlocal r, c
            for _ in range(steps):
                r += dr
                c += dc
                res.append(matrix[r][c])

        while len(res) < (rows * cols):
            move(col, 0, 1)
            move(row, 1, 0)

            col = col - 1 if flag else col

            move(col, 0, -1)
            move(row - 1, -1, 0)

            row -= 2
            col -= 1
            flag = True
        
        while len(res) != (rows * cols):
            res.pop()
        
        return res
    

    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        rows, cols = len(matrix), len(matrix[0])
        top, bottom, left, right = 0, rows, 0, cols
        res = []

        while top < bottom and left < right:
            for i in range(left, right):
                res.append(matrix[top][i])
            top += 1

            for i in range(top, bottom):
                res.append(matrix[i][right - 1])
            right -= 1

            if top >= bottom or left >= right:
                break

            for i in range(right - 1, left - 1, -1):
                res.append(matrix[bottom - 1][i])
            bottom -= 1

            for i in range(bottom - 1, top - 1, -1):
                res.append(matrix[i][left])
            left += 1
        
        return res