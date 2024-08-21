from typing import List


class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        dp = {}

        def dfs(alice, i, M):
            if i >= len(piles):
                return 0

            if (alice, i, M) in dp:
                return dp[(alice, i, M)]

            res = 0 if alice else float("inf")
            total = 0
            for n in range(1, (2 * M) + 1):
                if i + n > len(piles):
                    break
                
                total += piles[i + n - 1]
                if alice:
                    res = max(res, total + dfs(False, i + n, max(M, n)))
                else:
                    res = min(res, dfs(True, i + n, max(M, n)))

                dp[(alice, i, M)] = res
            return res

        return dfs(True, 0, 1)
    

    def stoneGameII(self, piles: List[int]) -> int:
        dp = [[0] * len(piles) for _ in range(len(piles))]
        suffix_sum = piles[:]

        for i in range(len(suffix_sum) - 2, -1, -1):
            suffix_sum[i] += suffix_sum[i + 1]

        def dfs(suffix_sum: List[int], M: int, i: int, dp: List[List[int]]) -> int:
            if i + 2 * M >= len(suffix_sum):
                return suffix_sum[i]

            if dp[i][M] > 0:
                return dp[i][M]

            res = float("inf")
            for n in range(1, 2 * M + 1):
                res = min(res, dfs(suffix_sum, max(n, M), i + n, dp))

            dp[i][M] = suffix_sum[i] - res
            return dp[i][M]

        return dfs(suffix_sum, 1, 0, dp)