class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)
    
    
    def strStr2(self, haystack: str, needle: str) -> int:
        
        if needle == "":
            return 0
        
        for i in range(len(haystack) + 1 - len(needle)):
            for j in range(len(needle)):
                if haystack[i + j] != needle[j]:
                    break
                if j == len(needle) - 1:
                    return i
        
        return -1
    

    def strStr3(self, haystack: str, needle: str) -> int:
        if needle == "":
            return 0
        
        for i in range(len(haystack) + 1 - len(needle)):
            if haystack[i: i + len(needle)] == needle:
                return i
        
        return -1
    

    # Knuth - Morris - Pratt (KMP) Algorithm
    def kmp_search(self, h, n):
        def compute_lps(n):
            lps = [0] * len(n)
            length = 0
            i = 1
            while i < len(n):
                if n[i] == n[length]:
                    length += 1
                    lps[i] = length
                    i += 1
                else:
                    if length != 0:
                        length = lps[length - 1]
                    else:
                        lps[i] = 0
                        i += 1
            return lps
        
        h_len = len(h)
        n_len = len(n)
        
        if n_len == 0:
            return 0
        
        lps = compute_lps(n)
        i = 0
        j = 0
        while i < h_len:
            if h[i] == n[j]:
                i += 1
                j += 1
            
            if j == n_len:
                return i - j
            elif i < h_len and h[i] != n[j]:
                if j != 0:
                    j = lps[j - 1]
                else:
                    i += 1
        
        return -1


sol = Solution()
h = "mississippi"
n = "issip"
print(sol.strStr3(haystack=h, needle=n))

# Knuth - Morris - Pratt (KMP) Algorithm
h = "mississippi"
n = "issip"
index = sol.kmp_search(h, n)
print(f"KMP algorihm result: {index}")  # Output: 4
