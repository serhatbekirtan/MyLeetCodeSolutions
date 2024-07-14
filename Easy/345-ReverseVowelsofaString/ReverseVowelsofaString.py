class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = set("aeiouAEIOU")
        chars = list(s)

        i = 0
        j = len(chars) - 1
        L = ""
        R = ""

        while i < j:
            if chars[i] in vowels:
                L = chars[i]
            else:
                i += 1
            
            if chars[j] in vowels:
                R = chars[j]
            else:
                j -= 1

            if L and R:
                chars[i], chars[j] = R, L
                i += 1
                j -= 1
                L = ""
                R = ""

        return (''.join(chars))