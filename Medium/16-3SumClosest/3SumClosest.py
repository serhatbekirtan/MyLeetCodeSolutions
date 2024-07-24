from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        result = float('inf')

        for i in range(len(nums)):
            L = i + 1
            R = len(nums) - 1

            while L < R:
                total = nums[i] + nums[L] + nums[R]
                if abs(target - total) < abs(target - result):
                    result = total

                if total < target:
                    L += 1
                elif total > target:
                    R -= 1
                else:
                    return target

        return result