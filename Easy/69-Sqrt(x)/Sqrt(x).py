class Solution:
    def mySqrt(self, x: int) -> int:

        half = x // 2
        for i in range(half + 2):
            square = i * i
            if square == x:
                return i
            if square > x:
                return i - 1
            
    
    def mySqrt2(self, x: int) -> int:
        left = 0
        right = (x // 2) + 2

        while left < right:
            mid = (left + right) // 2
            if x == (mid * mid):
                return mid
            
            elif x < (mid * mid):
                right = mid - 1
            
            else:
                left = mid + 1

        if (left * left) > x:
            return left - 1
        
        if (left * left) <= x:
            return left
        
        return x