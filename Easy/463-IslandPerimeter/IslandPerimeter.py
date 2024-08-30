from typing import List


class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])

        def countPerimeters(r, c):
            directions = [[r + 1, c], [r - 1, c], [r, c + 1], [r, c - 1]]
            count = 0
            
            for nr, nc in directions:
                if nr < 0 or nc < 0 or nr == rows or nc == cols or grid[nr][nc] == 0:
                    count += 1

            return count

        res = 0
        for row in range(rows):
            for col in range(cols):
                if grid[row][col]:
                    res += countPerimeters(row, col)

        return res