class Solution:
    def hammingWeight(self, n: int) -> int:
        total = 0

        while n:

            if n & 1 == 1:
                total += 1

            n >>= 1

        return total