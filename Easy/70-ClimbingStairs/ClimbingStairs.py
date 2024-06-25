class Solution:
    def climbStairs(self, n: int) -> int:
        dynamic_arr = [0, 1]

        if n == 0:
            return 0

        if n == 1:
            return 1

        for i in range(n):
            dynamic_arr.append(dynamic_arr[i] + dynamic_arr[i + 1])

        return dynamic_arr[len(dynamic_arr) - 1]
    

    def climbStairsRecursive(self, n: int) -> int:
        if n == 0:
            return 0
        
        if n == 1:
            return 1
        
        if n == 2:
            return 2
        
        if n > 0:
            take_1 = Solution.climbStairs(self, n - 1)
            take_2 = Solution.climbStairs(self, n - 2)        

        return take_1 + take_2