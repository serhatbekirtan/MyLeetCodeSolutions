class Solution:
    def isUgly(self, n: int) -> bool:
        if not n:
            return False
        
        while n % 5 == 0:
            n = n // 5

        while n % 3 == 0:
            n = n // 3
            
        while n % 2 == 0:
            n = n // 2

        return n == 1
    

    # Cleaner iteration:
    """
    for i in [5,3,2]:
        while n % i == 0:
            n = n // i

    """