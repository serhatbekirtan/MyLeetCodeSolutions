class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        L = 1
        R = num

        while L <= R:
            mid = (L + R) // 2
            mid_square = mid * mid

            if mid_square == num:
                return mid

            if mid_square < num:
                L = mid + 1
            else:
                R = mid - 1

        return False