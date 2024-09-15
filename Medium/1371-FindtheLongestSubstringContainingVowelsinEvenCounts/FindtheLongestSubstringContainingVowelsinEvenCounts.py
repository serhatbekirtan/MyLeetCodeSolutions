class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        vowels = {'a': 1, 'e': 2, 'i': 4, 'o': 8, 'u': 16}
        maskMap, xor, res = {0: -1}, 0, 0

        for i, c in enumerate(s):
            if c in vowels:
                xor ^= vowels[c]

            if xor not in maskMap:
                maskMap[xor] = i
            else:
                res = max(res, i - maskMap[xor])
        
        return res