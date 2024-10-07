class Solution:
    def minLength(self, s: str) -> int:
        while "AB" in s or "CD" in s:
            while "AB" in s:
                indexAB = s.find("AB")
                if indexAB >= 0:
                    s = s[:indexAB] + s[indexAB + 2:]
            while "CD" in s:
                indexCD = s.find("CD")
                if indexCD >= 0:
                    s = s[:indexCD] + s[indexCD + 2:]
        return len(s)
    

    def minLength(self, s: str) -> int:
        stack = []

        for c in s:
            if len(stack) > 0 and ((stack[-1] == 'A' and c == 'B') or(stack[-1] == 'C' and c == 'D')):
                stack.pop()
            else:
                stack.append(c)
        
        return len(stack)