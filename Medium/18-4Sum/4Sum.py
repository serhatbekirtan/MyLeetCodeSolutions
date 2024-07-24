from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        result = set()

        for i in range(len(nums) - 3):
            for j in range(i + 2, len(nums)):
                L = i + 1
                R = j - 1
                total = 0

                while L < R:
                    total = nums[i] + nums[j] + nums[L] + nums[R]
                    if total > target:
                        R -= 1
                    elif total < target:
                        L += 1
                    else:
                        result.add((nums[i], nums[L], nums[R], nums[j]))
                        R -= 1

        return result
    

    # A generic recursive solution for Ksum problems.
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        result = []
        quad = []

        def kSum(k, start, target):
            if k != 2:
                for i in range(start, len(nums) - k + 1):
                    if i > start and nums[i] == nums[i - 1]:
                        continue

                    quad.append(nums[i])
                    kSum(k - 1, i + 1, target - nums[i])
                    quad.pop()
                return
            
            L = start
            R = len(nums) - 1

            while L < R:
                if nums[L] + nums[R] < target:
                    L += 1
                elif nums[L] + nums[R] > target:
                    R -= 1
                else:
                    result.append(quad + [nums[L], nums[R]])
                    L += 1

                    while L < R and nums[L] == nums[L - 1]:
                        L += 1

        kSum(4, 0, target)
        return result