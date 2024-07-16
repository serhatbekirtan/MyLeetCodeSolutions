class Solution:
    def arrangeCoins(self, n: int) -> int:
        total = 0
        
        i = 0
        while total < n:
            i += 1
            total += i

            if total > n:
                return i - 1

        return i
    

    def arrangeCoinsBinarySearch(self, n: int) -> int:
        L = 0
        R = n

        while L <= R:
            mid = (L + R) // 2
            formula = ((mid * (mid + 1)) // 2)
            
            if formula == n:
                return mid

            if formula > n:
                R = mid - 1

            if formula < n:
                L = mid + 1

        return R