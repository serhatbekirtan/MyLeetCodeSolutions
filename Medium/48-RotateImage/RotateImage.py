from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix) - 1
        i, j = 0, 0

        while i < (n - i):
            k = j
            while j < (n - i):
                temp = matrix[j][n - i]
                matrix[j][n - i] = matrix[i][j]
                temp2 = matrix[n - i][n - j]
                matrix[n - i][n - j] = temp
                temp3 = matrix[n - j][i]
                matrix[n - j][i] = temp2
                matrix[i][j] = temp3
                j += 1
                
            i += 1
            j = k + 1

            
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix) - 1
        i, j = 0, 0

        while i < (n - i):
            k = j
            while j < (n - i):
                temp = matrix[i][j]

                matrix[i][j] = matrix[n - j][i]
                matrix[n - j][i] = matrix[n - i][n - j]
                matrix[n - i][n - j] = matrix[j][n - i]
                matrix[j][n - i] = temp

                j += 1
                
            i += 1
            j = k + 1