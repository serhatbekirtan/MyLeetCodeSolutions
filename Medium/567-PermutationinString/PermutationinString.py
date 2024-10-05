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
    

    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1, n2 = len(s1), len(s2)
        if n1 > n2:
            return False

        s1Count, s2Count = [0] * 26, [0] * 26
        for i in range(n1):
            s1Count[ord(s1[i]) - ord('a')] += 1
            s2Count[ord(s2[i]) - ord('a')] += 1

        matches = 0
        for i in range(26):
            matches += 1 if s1Count[i] == s2Count[i] else 0

        L = 0
        for R in range(n1, n2):
            if matches == 26:
                return True
            
            index = ord(s2[R]) - ord('a')
            s2Count[index] += 1
            if s1Count[index] == s2Count[index]:
                matches += 1
            elif s1Count[index] + 1 == s2Count[index]:
                matches -= 1

            index = ord(s2[L]) - ord('a')
            s2Count[index] -= 1
            if s1Count[index] == s2Count[index]:
                matches += 1
            elif s1Count[index] - 1 == s2Count[index]:
                matches -= 1
            
            L += 1

        return matches == 26