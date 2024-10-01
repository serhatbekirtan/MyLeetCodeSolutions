from collections import defaultdict
from typing import List


class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        hashmap = defaultdict(int)
        for num in arr:
            hashmap[num % k] += 1

        for remainder in hashmap:
            if remainder == k - remainder or remainder == 0:
                if hashmap[remainder] % 2 != 0:
                    return False
            elif hashmap[remainder] != hashmap[k - remainder]:
                return False

        return True