from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []

        def backtrack(open, close, string):
            if open + close == n * 2:
                result.append(string)
                return

            if open < n:
                backtrack(open + 1, close, string + "(")
            
            if close < open:
                backtrack(open, close + 1, string + ")")

        backtrack(0, 0, "")
        return result