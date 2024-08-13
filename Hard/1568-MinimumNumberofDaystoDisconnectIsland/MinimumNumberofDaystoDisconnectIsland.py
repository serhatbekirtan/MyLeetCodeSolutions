from typing import List


class Solution:
    def minDays(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])

        def dfs(r, c, visit):
            if (r < 0 or c < 0 or r == rows or c == cols or 
                grid[r][c] == 0 or (r, c) in visit):
                return

            visit.add((r, c))
            neighbors = [[r + 1, c], [r - 1, c], [r, c + 1], [r, c - 1]]
            for nr, nc in neighbors:
                dfs(nr, nc, visit)

        def countIslands():
            visit = set()
            count = 0
            for row in range(rows):
                for col in range(cols):
                    if grid[row][col] and (row,col) not in visit:
                        dfs(row, col, visit)
                        count += 1
            return count

        if countIslands() != 1:
            return 0

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 0:
                    continue
                
                grid[row][col] = 0
                if countIslands() != 1:
                    return 1
                grid[row][col] = 1

        return 2