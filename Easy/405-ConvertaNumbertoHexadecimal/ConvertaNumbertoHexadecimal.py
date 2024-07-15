class Solution:
    def toHex(self, num: int) -> str:
        if num == 0:
            return "0"
    
        if num < 0:
            num += 2**32
        
        result = ""

        while num:
            digit = num % 16
            if digit > 9:
                result += chr(87 + digit)
            else:
                result += str(digit)
            num = num // 16

        return result[::-1]
    
    # "a" ASCII value is 97.
    # "A" ASCII value is 65
    # Could also use a map = '0123456789abcdef'