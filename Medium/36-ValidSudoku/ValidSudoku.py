from typing import List
from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        for row in range(9):
            for column in range(9):
                value = board[row][column]

                if not value.isdigit():
                    continue

                for col in range(column + 1, 9):
                    if value == board[row][col]:
                        return False

                for ro in range(row + 1, 9):
                    if value == board[ro][column]:
                        return False

                i = row
                j = column
                while i % 3 != 2 or j % 3 != 2:
                    if j % 3 == 2:
                        i += 1
                        j -= 2
                    else:
                        j += 1

                    if not board[i][j].isdigit():
                        continue
                    
                    if value == board[i][j]:
                        return False

        return True
    

    # Cleaner Solution using hashmaps and sets.
    def isValidSudoku2(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        squares = defaultdict(set)

        for row in range(9):
            for col in range(9):
                if not board[row][col].isdigit():
                    continue

                if (board[row][col] in rows[row] or 
                    board[row][col] in cols[col] or 
                    board[row][col] in squares[(row // 3, col // 3)]):
                    return False
                
                rows[row].add(board[row][col])
                cols[col].add(board[row][col])
                squares[(row // 3, col // 3)].add(board[row][col])
    
        return True