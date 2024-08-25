class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        binX = bin(x)[2:] # 101 
        binY = bin(y)[2:] # 1

        difference = abs(len(binX) - len(binY)) # 2

        if len(binX) > len(binY):
            binY = ("0" * difference) + binY
        else:
            binX = ("0" * difference) + binX

        res = 0

        for i, j in zip(binX, binY):
            if i != j:
                res += 1

        return res
    

    def hammingDistance(self, x: int, y: int) -> int:
        return int.bit_count(x ^ y)