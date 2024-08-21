from typing import Counter, List


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        hashmap = Counter(nums)
        res = []

        for i in range(1, len(nums) + 1):
            if i not in hashmap:
                res.append(i)

        return res
    

    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        res = []

        for i in range(len(nums)):
            num = abs(nums[i]) - 1
            if nums[num] > 0: 
                nums[num] *= -1

        for i, num in enumerate(nums):
            if num > 0:
                res.append(i + 1)

        return res