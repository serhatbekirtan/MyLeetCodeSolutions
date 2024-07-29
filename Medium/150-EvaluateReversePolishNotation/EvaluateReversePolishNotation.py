from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        def performOperation(firstVal, secondVal, operation):
            if operation == "+":
                return firstVal + secondVal
            elif operation == "-":
                return secondVal - firstVal
            elif operation == "*":
                return firstVal * secondVal
            else:
                return int(secondVal / firstVal)

        operationMap = set(("+", "-", "*", "/"))
        stack = []

        for token in tokens:
            if token in operationMap:
                first, second = stack.pop(), stack.pop()
                result = performOperation(first, second, token)
                stack.append(result)
            else:
                stack.append(int(token))

        return stack[0]
    

    # Cleaner, maybe?
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            if token == "+":
                stack.append(stack.pop() + stack.pop())
            elif token == "-":
                first, second = stack.pop(), stack.pop()
                stack.append(second - first)
            elif token == "*":
                stack.append(stack.pop() * stack.pop())
            elif token == "/":
                first, second = stack.pop(), stack.pop()
                stack.append(int(second / first))
            else:
                stack.append(int(token))

        return stack[0]