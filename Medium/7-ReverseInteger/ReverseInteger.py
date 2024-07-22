class Solution:
    def reverse(self, x: int) -> int:
        str_int = str(x)
        if str_int[0] == "-":
            str_int = str_int[1:len(str_int)]
            str_int += "-"

        str_int = str_int[::-1]
        int_str = int(str_int)
        
        return int_str if (-pow(2, 31)) < int_str < (pow(2, 31) - 1) else 0
    

    # Solution without using int() or str()
    def reverse(self, x: int) -> int:
        sign = 1 if x > 0 else -1
        reverse = 0
        x = abs(x)

        while x:

            reverse *= 10
            digit = x % 10
            reverse += digit

            if reverse > (pow(2, 31) - 1):
                return 0

            x //= 10

        return sign * reverse
    

    # Solution to not exceed 32 bit integers.
    def reverse(self, x: int) -> int:
        MAX = (2 ** 31) - 1

        result = 0
        sign = 1 if x > 0 else -1
        x = abs(x)

        while x:
            digit = x % 10
            x = x // 10

            if ((result > MAX // 10) or (result == MAX // 10) and (digit >= MAX % 10)):
                return 0
            
            result = (result * 10) + digit

        return result if sign > 0 else -result