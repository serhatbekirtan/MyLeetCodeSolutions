from collections import Counter
from typing import List


class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        hashmap = Counter(arr)
        count = 0
        for s in arr:
            if hashmap[s] == 1:
                count += 1
                if count == k:
                    return s
        
        return ""