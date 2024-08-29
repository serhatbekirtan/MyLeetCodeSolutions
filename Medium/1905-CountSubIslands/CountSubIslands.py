from typing import List


class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        rows, cols = len(grid1), len(grid1[0])

        def dfs(r, c, island, visit):
            if (r < 0 or c < 0 or r == rows or c == cols or grid2[r][c] == 0 or (r,c) in visit):
                return
            
            visit.add((r,c))
            island.append([r,c])
            neighbors = [[r, c + 1], [r, c - 1], [r + 1, c], [r - 1, c]]
            for nr, nc in neighbors:
                dfs(nr, nc, island, visit)
            
            return island

        visit = set()
        islands = []
        for row in range(rows):
            for col in range(cols):
                if grid2[row][col] and (row, col) not in visit:
                    islands.append(dfs(row, col, [], visit))

        res = len(islands)
        for island in islands:
            for row, col in island:
                if not grid1[row][col]:
                    res -= 1
                    break

        return res
    

    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        rows, cols = len(grid1), len(grid1[0])

        def dfs(r, c):
            if (r < 0 or c < 0 or r == rows or c == cols or grid2[r][c] == 0):
                return
            
            grid2[r][c] = 0
            neighbors = [[r, c + 1], [r, c - 1], [r + 1, c], [r - 1, c]]
            for nr, nc in neighbors:
                dfs(nr, nc)

        for row in range(rows):
            for col in range(cols):
                if grid2[row][col] and not grid1[row][col]:
                    dfs(row, col)

        res = 0
        for row in range(rows):
            for col in range(cols):
                if grid2[row][col]:
                    dfs(row, col)
                    res += 1

        return res