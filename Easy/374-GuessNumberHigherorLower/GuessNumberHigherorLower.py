# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
def guess(num: int) -> int:
    return num

class Solution:
    def guessNumber(self, n: int) -> int:
        L = 1
        R = n

        while L <= R:
            num = (L + R) // 2

            if guess(num) == 1:
                L = num + 1
            
            elif guess(num) == -1:
                R = num - 1

            else:
                return num