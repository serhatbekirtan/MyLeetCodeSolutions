class Solution:
    def findComplement(self, num: int) -> int:
        temp = num
        power = 0
        while temp:
            temp //= 2
            power += 1

        return num ^ (2 ** power) - 1


    def findComplement(self, num: int) -> int:
        bitLength = num.bit_length()
        
        mask = (1 << bitLength) - 1
        
        return num ^ mask