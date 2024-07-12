# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        L = 0
        R = n

        while L + 1 < R:
            M = (L + R) // 2

            if isBadVersion(M):
                R = M
            else:
                L = M

        return R