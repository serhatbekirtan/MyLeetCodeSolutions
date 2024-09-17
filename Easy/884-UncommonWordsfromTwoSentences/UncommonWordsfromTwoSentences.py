from collections import Counter
from typing import List


class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        arr1, arr2 = s1.split(), s2.split()
        freq1, freq2 = Counter(arr1), Counter(arr2)
        res = []

        for word in arr1:
            if word not in freq2 and freq1[word] == 1:
                res.append(word)
        
        for word in arr2:
            if word not in freq1 and freq2[word] == 1:
                res.append(word)

        return res
    

    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        freq = Counter(s1.split() + s2.split())
        res = []

        for word, count in freq.items():
            if count == 1:
                res.append(word)

        return res
    

    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        return [word for word, count in Counter(s1.split() + s2.split()).items() if count == 1]