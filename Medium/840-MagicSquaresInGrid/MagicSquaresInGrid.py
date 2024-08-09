from typing import List


class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        def magic(row, col):
            values = set()
            for i in range(row, row + 3):
                for j in range(col, col + 3):
                    if grid[i][j] in values or not (1 <= grid[i][j] <= 9):
                        return 0
                    values.add(grid[i][j])

            # Check col sums
            if grid[row][col] + grid[row][col + 1] + grid[row][col + 2] != 15:
                return 0

            # Check row sums
            if grid[row][col] + grid[row + 1][col] + grid[row + 2][col] != 15:
                return 0

            # Check diagonal sums
            if (grid[row][col] + grid[row + 1][col + 1] + grid[row + 2][col + 2] != 15 or 
                grid[row][col + 2] + grid[row + 1][col + 1] + grid[row + 2][col] != 15):
                return 0

            return 1
        
        res = 0
        for row in range(len(grid) - 2):
            for col in range(len(grid[0]) - 2):
                res += magic(row, col)

        return res
    

    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        res = 0
        pattern1 = "438167294381672"
        pattern2 = "927618349276183"

        def magic(row, col):
            if grid[row][col] != 5:
                return 0
            
            neighbors = [
                [row - 1, col], [row - 1, col + 1],
                [row, col + 1], [row + 1, col + 1],
                [row + 1, col], [row + 1, col - 1],
                [row, col - 1], [row - 1, col - 1]
            ]

            sequence = ""

            for nr1, nr2 in neighbors:
                sequence += str(grid[nr1][nr2])
            
            if sequence in pattern1 or sequence in pattern2:
                return 1
            
            return 0
        
        for row in range(1, ROWS - 1):
            for col in range(1, COLS - 1):
                res += magic(row, col)
        
        return res