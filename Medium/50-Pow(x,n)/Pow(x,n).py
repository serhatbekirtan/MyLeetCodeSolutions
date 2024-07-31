from functools import cache


class Solution:
    @cache
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if n == 1:
            return x
        if n == -1:
            return 1 / x
        
        return self.myPow(x * x, n // 2) * self.myPow(x, n % 2)
    

    def myPow(self, x: float, n: int) -> float:
        def recursive(x, n):
            if x == 0:
                return 0
            if n == 0:
                return 1
            if n == 1:
                return x
            
            result = recursive(x * x, n // 2)
            return result if (n % 2 == 0) else (x * result)
            
        result = recursive(x, abs(n))
        return result if n >= 0 else 1 / result