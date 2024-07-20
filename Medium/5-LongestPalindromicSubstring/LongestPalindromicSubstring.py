class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest = ""

        for i in range(len(s)):
            for j in range(i, len(s)):
                substr = (s[i:j + 1])
                if substr == substr[::-1] and len(substr) > len(longest):
                    longest = substr
                    print(longest)

        return longest
    

    def longestPalindromeExpandMid(self, s: str) -> str:
        self.longest = ""
        self.length = 0
        
        def checkPalindrome(L, R):
            while L >= 0 and R < len(s) and s[L] == s[R]:
                if (R - L + 1) > self.length:
                    self.longest = s[L:R + 1]
                    self.length = R - L + 1
                
                L -= 1
                R += 1

        for i in range(len(s)):
            checkPalindrome(i, i)
            checkPalindrome(i, i + 1)

        return self.longest