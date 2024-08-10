from collections import deque
from typing import List


class Solution:
    directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

    def floodfill(self, expandedGrid, row, col):
        n = len(expandedGrid)
        queue = deque()
        queue.append([row, col])
        expandedGrid[row][col] = 1

        while queue:
            currRow, currCol = queue.popleft()
            for x, y in self.directions:
                newRow = currRow + x
                newCol = currCol + y

                if 0 <= newRow < n and 0 <= newCol < n and expandedGrid[newRow][newCol] == 0:
                    expandedGrid[newRow][newCol] = 1
                    queue.append((newRow, newCol))


    def regionsBySlashes(self, grid: List[str]) -> int:
        n = len(grid)
        expandedGrid = [[0] * (3 * n) for _ in range(3 * n)]
        baseRow = regionCount = 0

        for i in range(n):
            baseCol = 0
            for j in range(n):
                if grid[i][j] == "/":
                    expandedGrid[baseRow + 2][baseCol] = expandedGrid[baseRow + 1][baseCol + 1] = expandedGrid[baseRow][baseCol + 2] = 1
                elif grid[i][j] == "\\":
                    expandedGrid[baseRow][baseCol] = expandedGrid[baseRow + 1][baseCol + 1] = expandedGrid[baseRow + 2][baseCol + 2] = 1
                baseCol += 3
            baseRow += 3
        
        for i in range(len(expandedGrid)):
            for j in range(len(expandedGrid)):
                if expandedGrid[i][j] == 0:
                    self.floodfill(expandedGrid, i, j)
                    regionCount += 1
        
        return regionCount
    

sol = Solution()
print(sol.regionsBySlashes(grid=["/\\","\\/"]))