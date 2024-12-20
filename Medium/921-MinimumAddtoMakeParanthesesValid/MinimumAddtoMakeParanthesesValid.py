class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack = []
        for c in s:
            stack.append(c)
            if len(stack) > 1 and (stack[-1] == ')' and stack[-2] == '('):
                stack.pop()
                stack.pop()
        
        return len(stack)      
    
    
    def minAddToMakeValid(self, s: str) -> int:
        open_c = close_c = 0
        for c in s:
            if c == '(':
                open_c += 1
            elif c == ')' and open_c > 0:
                open_c -= 1
            else:
                close_c += 1
        return open_c + close_c