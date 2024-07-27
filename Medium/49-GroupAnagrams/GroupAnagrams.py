from typing import List
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_strs = []
        result = []

        for i, letter in enumerate(strs):
            sorted_strs.append(("".join(sorted(letter)), i))
        
        sorted_strs.sort()
        i = 0

        while i < len(sorted_strs):
            temp = []
            temp.append(strs[sorted_strs[i][1]])
            i += 1
            
            while i < len(sorted_strs) and sorted_strs[i - 1][0] == sorted_strs[i][0]:
                temp.append(strs[sorted_strs[i][1]])
                i += 1
            
            result.append(temp)

        return result
    

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)

        for letter in strs:
            count = [0] * 26

            for char in letter:
                count[ord(char) - ord("a")] += 1
            
            result[tuple(count)].append(letter)
        
        return result.values()