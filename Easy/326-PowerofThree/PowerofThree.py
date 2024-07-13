class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if not n:
            return False

        while n % 3 == 0:
            n = n // 3
            
        return n == 1
    

    # return n > 0 and 3**19 % n == 0

    # return n > 0 and 3**round(log(n, 3)) == n