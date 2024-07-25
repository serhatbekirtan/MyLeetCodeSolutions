import math


class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        absDividend = abs(dividend)
        absDivisor = abs(divisor)

        result = 0

        while absDividend >= absDivisor:
            temp = absDivisor
            multiply = 1

            while absDividend >= temp:
                absDividend -= temp
                result += multiply
                
                multiply += multiply
                temp += temp

        if (dividend < 0 and divisor >= 0) or (divisor <0 and dividend >= 0):
            result = -result

        return min((2 ** 31 - 1), max(-(2 ** 31), result))