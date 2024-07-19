class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sub = ""
        longest = 0
        i = 0
        j = 0

        while j < len(s):
            if i < len(s) and s[i] not in sub:
                sub += s[i]
                i += 1

            else:
                if len(sub) > longest:
                    longest = len(sub)
                j += 1
                if j < len(s): sub = s[j]
                i = j + 1

        return longest if longest > len(sub) else len(sub)
    
    # O(n)
    def legthOfLongestSubstringOptimal(self, s: str) -> int:
        result = 0
        hashset = set()
        L = 0

        for R in range(len(s)):
            while s[R] in hashset:
                hashset.remove(s[R])
                L += 1
            
            hashset.add(s[R])
            # result = max(result, R - L + 1) is also viable
            result = max(result, len(hashset))

        return result