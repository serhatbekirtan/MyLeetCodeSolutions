from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        L = 0
        R = len(numbers) - 1

        while L < R:
            add = numbers[L] + numbers[R]
            if add < target:
                L += 1
            elif add > target:
                R -= 1
            else:
                return [L + 1, R + 1]