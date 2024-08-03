from collections import Counter, defaultdict
from typing import List


class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        if arr == target:
            return True

        hashmapArr = Counter(arr)
        hashmapTarget = Counter(target)

        for key in hashmapArr:
            if key not in hashmapTarget or hashmapArr[key] != hashmapTarget[key]:
                return False

        return True


    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        hashmap = defaultdict(int)

        for key1, key2 in zip(target, arr):
            hashmap[key1] += 1
            hashmap[key2] -= 1

        for key in hashmap:
            if hashmap[key] != 0:
                return False
        
        return False
