from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        result = set()

        for i, num in enumerate(nums):

            target = -num
            L = i + 1
            R = len(nums) - 1

            while L < R:
                if nums[L] + nums[R] < target:
                    L += 1
                elif nums[L] + nums[R] > target:
                    R -= 1
                else:
                    result.add((num, nums[L], nums[R]))
                    R -= 1
            
        return list(result)


    # Directly Uses list.
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        result = []

        for i, num in enumerate(nums):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            target = -num
            L = i + 1
            R = len(nums) - 1

            while L < R:
                if nums[L] + nums[R] < target:
                    L += 1
                elif nums[L] + nums[R] > target:
                    R -= 1
                else:
                    result.append([num, nums[L], nums[R]])
                    R -= 1
                    while nums[R] == nums[R + 1] and L < R:
                        R -= 1
            
        return result