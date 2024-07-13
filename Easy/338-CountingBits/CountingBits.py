from typing import List


class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = []

        for i in range(n + 1):
            bits = i.bit_count()
            ans.append(bits)

        return ans
    

    # Linear Time O(n) solution with Dynamic Programming
    def countBits(self, n: int) -> List[int]:
        dp = [0]
        power = 0

        for i in range(1, n + 1):
            if (i & (i - 1)) == 0:
                power += 1

            bit_count = 1 + dp[i - 2 ** power]
            dp.append(bit_count)
        
        return dp