from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        mapping = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        result = []
        
        def backtrack(i, currentString):
            if len(currentString) == len(digits):
                result.append(currentString)
                return
            
            for c in mapping[digits[i]]:
                backtrack(i + 1, currentString + c)

        if digits:
            backtrack(0, "")

        return result