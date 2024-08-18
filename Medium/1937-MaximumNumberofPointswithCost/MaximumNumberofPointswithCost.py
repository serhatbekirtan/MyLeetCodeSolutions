from typing import List

class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        rows, cols = len(points), len(points[0])
        dp = points[0]

        for row in range(1, rows):
            nextRow = points[row].copy()

            left, right = [0] * cols, [0] * cols

            left[0] = dp[0]
            for col in range(1, cols):
                left[col] = max(dp[col], left[col - 1] - 1)

            right[cols - 1] = dp[cols - 1]
            for col in range(cols - 2, -1, -1):
                right[col] = max(dp[col], right[col + 1] - 1)

            for col in range(cols):
                nextRow[col] += max(left[col], right[col])

            dp = nextRow

        return max(dp)