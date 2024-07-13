class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if not n:
            return False
            
        while n % 4 == 0:
            n = n // 4

        return n == 1
    
    # return n > 0 and log(n, 4) % 1 == 0