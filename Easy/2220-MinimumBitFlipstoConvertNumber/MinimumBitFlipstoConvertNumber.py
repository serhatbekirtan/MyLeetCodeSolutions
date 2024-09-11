class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        res = 0
        src = bin(start)[2:]
        dst = bin(goal)[2:]
        smaller = bin(min(start, goal))[2:]
        shift = abs(len(src) - len(dst))
        
        for _ in range(shift):
            smaller = '0' + smaller

        if start < goal:
            src = smaller
        else:
            dst = smaller

        for i in range(len(src)):
            if src[i] != dst[i]:
                res += 1

        return res
    

    def minBitFlips(self, start: int, goal: int) -> int:
        count = 0 

        while start or goal:
            if start%2 != goal%2: 
                count+=1
            start, goal = start//2, goal//2

        return count
    

    def minBitFlips(self, start: int, goal: int) -> int:
        return (start ^ goal).bit_count()