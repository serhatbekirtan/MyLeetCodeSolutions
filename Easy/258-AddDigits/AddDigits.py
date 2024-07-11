class Solution:
    def addDigits(self, num: int) -> int:

        while num > 9:
            result = 0

            while num:
                digit = num % 10
                result += digit
                num = num // 10

            num = result
        
        return num
    

    # Alternate mathematical, O(1) solution:
    def addDigits(self, num: int) -> int:
        if not num:
            return 0
        
        return (num % 9) or 9