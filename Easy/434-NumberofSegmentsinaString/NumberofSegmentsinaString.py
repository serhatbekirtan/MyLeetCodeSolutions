class Solution:
    def countSegments(self, s: str) -> int:
        return len(s.split())
    

    def countSegments(self, s: str) -> int:
        result = []

        i = 0
        while i < len(s):
            letter = ""
            
            while i < len(s) and s[i] != " ":
                letter += s[i]
                i += 1

            if letter:
                result.append(letter)

            i += 1

        return len(result)
    

    def countSegments(self, s: str) -> int:
        segments = 0
        i = 0
        s += " "

        while i < len(s) - 1:
            if s[i] != ' ' and s[i+1] == ' ':
                segments += 1
                
            i += 1
        return segments