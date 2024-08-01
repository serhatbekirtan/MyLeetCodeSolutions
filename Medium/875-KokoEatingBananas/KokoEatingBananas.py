import math
from typing import List


class Solution:
    # O(log(max(n))*n) Time. O(1) Space.
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        L, R = 1, max(pile)
        result = R

        if len(piles) == h:
            return result

        while L <= R:
            rate = (L + R) // 2
            hours = 0
            for pile in piles:
                hours += math.ceil(pile / rate)

            if hours <= h:
                result = min(result, rate)
                R = rate - 1
            elif hours > h:
                L = rate + 1

        return result