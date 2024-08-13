from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def backtrack(index: int, curr: List[int], sum: int):
            if sum == target:
                res.append(curr.copy())
                return
            if sum > target:
                return

            for i in range(index, len(candidates)):
                if i > index and candidates[i - 1] == candidates[i]:
                    continue

                curr.append(candidates[i])
                backtrack(i + 1, curr, sum + candidates[i])
                curr.pop()

        backtrack(0, [], 0)
        return res


    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def backtrack(i: int, curr: List[int], sum: int):
            if sum == target:
                res.append(curr.copy())
                return
            if sum > target or i == len(candidates):
                return

            curr.append(candidates[i])
            backtrack(i + 1, curr, sum + candidates[i])
            curr.pop()

            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1
            backtrack(i + 1, curr, sum)

        backtrack(0, [], 0)
        return res