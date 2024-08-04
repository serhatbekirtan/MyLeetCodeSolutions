from collections import Counter


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        hashmap1 = Counter(s1)
        L = 0

        for R in range(len(s1), len(s2) + 1):
            currMap = Counter(s2[L:R])
            if hashmap1 == currMap:
                return True
            L += 1

        return False

    
    def checkInclusion(self, s1: str, s2: str) -> bool:
        hashmap = Counter(s1)
        L = 0
        count = 0

        for R in range(len(s2)):
            if s2[R] in hashmap:
                hashmap[s2[R]] -= 1
                if hashmap[s2[R]] == 0:
                    count += 1
            
            if R - L >= len(s1) and s2[L] in hashmap:
                if hashmap[s2[L]] == 0:
                    count -= 1
                hashmap[s2[L]] += 1

            if R - L >= len(s1):
                L += 1

            if count == len(hashmap):
                return True

        return False