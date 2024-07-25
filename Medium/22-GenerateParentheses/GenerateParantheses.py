from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []

        def backtrack(num, stack, string):
            if not stack and len(string) == n * 2:
                result.append(string)
                return

            if len(stack) > 1:
                if stack[-1] == ")" and stack[-2] == "(":
                    stack.pop()
                    stack.pop()

            for i in range(num):
                backtrack(num - 1, stack.append("("), string + "(")
                backtrack(num - 1, stack.append(")"), string + ")")
            

        backtrack(n, [], "")

        return result
    

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