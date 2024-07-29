from collections import defaultdict
from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []

        def backtrack(i: int, cur: List[int], total: int):
            print(cur)
            if total == target:
                result.append(cur.copy())
                return
            if i >= len(candidates) or total > target:
                return
            
            cur.append(candidates[i])
            backtrack(i, cur, total + candidates[i])
            cur.pop()
            backtrack(i + 1, cur, total)

        backtrack(0, [], 0)
        return result

    

sol = Solution()
candidates = [2,3,5]
target = 8
print(sol.combinationSum(candidates=candidates, target=target))