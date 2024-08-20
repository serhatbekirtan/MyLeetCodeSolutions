from typing import List


class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        return True
    

    def stoneGame(self, piles: List[int]) -> bool:
        dp = {}

        def dfs(L, R):
            if L > R:
                return 0
            
            if (L, R) in dp:
                return dp[(L, R)]
            
            even = True if (R- L) % 2 else False
            left = piles[L] if even else 0
            right = piles[R] if even else 0

            dp [(L, R)] = max(dfs(L + 1, R) + left, dfs(L, R - 1) + right)
            return dp[(L, R)]
        
        return dfs(0, len(piles) - 1) > sum(piles) // 2