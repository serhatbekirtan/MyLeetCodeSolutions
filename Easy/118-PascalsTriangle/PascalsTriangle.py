from typing import List

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        pascals = []
        
        for i in range(numRows):
            if i == 0:
                pascals.append([1])
                continue
            
            if i == 1:
                pascals.append([1, 1])
                continue

            pascals.append([1])
            
            for j in range(i - 1):
                pascals[i].append(pascals[i - 1][j] + pascals[i - 1][j + 1])
            
            pascals[i].append(1)

        return pascals