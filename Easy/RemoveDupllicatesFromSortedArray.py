from typing import List


class Solution:
    def removeDuplicates1(self, nums: List[int]) -> int:
        unique = 0
        checker = 1

        while checker < len(nums):
            if nums[unique] == nums[checker]:
                nums.pop(checker)
            else:
                unique = checker
                checker += 1

        return checker
    

    def removeDuplicates2(self, nums: List[int]) -> int:
        unique = 0
        checker = 1

        while checker < len(nums):
            if nums[unique] == nums[checker]:
                checker += 1
            else:
                nums[unique + 1] = nums[checker]
                unique += 1
                checker += 1

        return unique + 1