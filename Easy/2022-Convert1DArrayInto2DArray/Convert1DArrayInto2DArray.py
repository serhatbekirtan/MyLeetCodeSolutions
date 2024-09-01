from typing import List


class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if m * n != len(original):
            return []

        res, cur = [], []

        for i, num in enumerate(original):
            cur.append(num)
            if i % n == n - 1:
                res.append(cur)
                cur = []
        
        return res
    

    # O(1) Space.
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if m * n != len(original):
            return []

        res = [[] for _ in range(m)]
        row = 0

        for i, num in enumerate(original):
            res[row].append(num)
            if i % n == n - 1:
                row += 1

        return res
        
