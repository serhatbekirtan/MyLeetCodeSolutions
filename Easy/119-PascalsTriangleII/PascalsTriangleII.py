from typing import List


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        
        pascals = []

        for i in range(rowIndex + 1):
            row = [1] * (i + 1)

            for j in range(1, i):
                row[j] = pascals[i - 1][j - 1] + pascals[i - 1][j]

            pascals.append(row)
        
        return pascals[rowIndex]


    def getRowOptimized(self, rowIndex: int) -> List[int]:
        result = [1] * (rowIndex + 1)
        
        for i in range(1, rowIndex):
            for j in range(i, 0, -1):
                result[j] += result[j - 1]

        return result

# [1, 1, 1]
# [1, 2, 1]

# [1, 1, 1, 1]
# [1, 2, 1, 1]
# [1, 2, 3, 1]
# [1, 3, 3, 1]

# [1, 2, 1, 1, 1]
# [1, 3, 3, 1, 1]
# [1, 4, 6, 4, 1]