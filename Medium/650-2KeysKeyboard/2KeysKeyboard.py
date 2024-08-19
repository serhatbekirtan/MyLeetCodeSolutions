class Solution:
    def minSteps(self, n: int) -> int:
        if n == 1:
            return 0

        res = []
        def backtrack(opCount, num, copyAmount):
            if num == n:
                res.append(opCount)
                return
            
            if num > n:
                return
                
            backtrack(opCount + 2, num + num, num) # Copy, Paste
            backtrack(opCount + 1, num + copyAmount, copyAmount) # Paste

        backtrack(1, 1, 1)
        return min(res)


    # Backtracking with cache.
    def minSteps(self, n: int) -> int:
        if n == 1:
                return 0

        cache = {}
        def backtrack(count, paste):
            if count == n:
                return 0
            
            if count > n:
                return 1000
            
            if (count, paste) in cache:
                return cache[(count, paste)]

            res1 = 1 + backtrack(count + paste, paste) # Copy, Paste
            res2 = 2 + backtrack(count + count, count) # Paste
            cache[(count, paste)] = min(res1, res2)
            return cache[(count, paste)]

        return 1 + backtrack(1, 1)

    
    # Dp solution.
    def minSteps(self, n: int) -> int:
        dp = [1000] * (n + 1)
        dp[1] = 0

        for i in range(2, n + 1):
            for j in range(1, 1 + (i // 2)):
                if i % j == 0:
                    dp[i] = min(dp[i], dp[j] + (i // j))

        return dp[n]