from typing import List


class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        totalRolls = len(rolls) + n
        sumOfTotalRolls = totalRolls * mean
        remainingSum = sumOfTotalRolls - sum(rolls)
        if not (1 <= remainingSum / n <= 6):
            return []

        res = [1 for _ in range(n)]
        sumOfRes = n
        for i in range(n):
            while res[i] < 6 and sumOfRes < remainingSum:
                res[i] += 1
                sumOfRes += 1

        return res