from typing import List


class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        right_down, left_up = 1, 2
        res = [[rStart, cStart]]

        while len(res) < (rows * cols):
            for i in range(right_down):
                cStart += 1
                if 0 <= self.col < cols and 0 <= self.row < rows:
                    res.append([rStart, cStart])
            
            for i in range(right_down):
                rStart += 1
                if 0 <= self.col < cols and 0 <= self.row < rows:
                    res.append([rStart, cStart])

            for i in range(left_up):
                cStart -= 1
                if 0 <= self.col < cols and 0 <= self.row < rows:
                    res.append([rStart, cStart])

            for i in range(left_up):
                rStart -= 1
                if 0 <= self.col < cols and 0 <= self.row < rows:
                    res.append([rStart, cStart])

            right_down += 2
            left_up += 2

        return res
    
    # Cleaner.
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        right_down, left_up = 1, 2
        self.row, self.col = rStart, cStart
        res = []

        def move(direction, times):
            for i in range(times):
                if 0 <= self.col < cols and 0 <= self.row < rows:
                    res.append([self.row, self.col])

                match direction:
                    case "right":
                        self.col += 1
                    case "down":
                        self.row += 1
                    case "left":
                        self.col -= 1
                    case "up":
                        self.row -= 1

        while len(res) < (rows * cols):
            move("right", right_down)
            move("down", right_down)
            move("left", left_up)
            move("up", left_up)

            right_down += 2
            left_up += 2

        return res
    
    #Cleanest.
    def spiralMatrixIII1(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        res = []
        row, col = rStart, cStart
        i, steps = 0, 1

        while len(res) < (rows * cols):
            for _ in range(2):
                deltaRow, deltaCol = directions[i]

                for _ in range(steps):
                    if (0 <= row < rows and 0 <= col < cols):
                        res.append([row, col])

                    row, col = row + deltaRow, col + deltaCol
                i = (i + 1) % 4
            steps += 1
        
        return res