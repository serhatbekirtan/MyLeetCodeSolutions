class Solution:
    def shortestPalindrome(self, s: str) -> str:
        prefix, suffix,  = 0, 0
        base, lastIndex, power, mod = 29, 0, 1, 10 ** 9 + 7

        for i, c in enumerate(s):
            char = ord(c) - ord('a') + 1
            prefix = ((prefix * base) + char) % mod
            suffix = (suffix + char * power) % mod
            power = (power * base) % mod

            if prefix == suffix:
                lastIndex = i
        
        suffix = s[lastIndex + 1:]
        return suffix[::-1] + s