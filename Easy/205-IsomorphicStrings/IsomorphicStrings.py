from typing import Counter


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        result_S = self.mapChars(t, s)
        result_T = self.mapChars(s, t)

        return result_S == s and result_T == t
    
    def mapChars(self, string1, string2) -> dict:
        i = 0
        map = {}
        result = ""

        while i < len(string1):
            k = string1[i]
            v = string2[i]
            map.update({k: v})
            i += 1

        for char in string1:
            result += map.get(char)

        return result

