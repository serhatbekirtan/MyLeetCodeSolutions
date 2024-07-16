import sys
from typing import List


class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums.sort()
        max_array = []
        max_number = -(2 ** 32)
        index = 0

        for num in nums:
            if num > max_number:
                max_array.append(num)
                max_number = num
                index += 1

        if len(max_array) < 3:
            return max_array[-1]

        return max_array[index - 3]
    

    def thirdMaxLinearTime(self, nums: List[int]) -> int:
        nums = list(set(nums))

        if len(nums) < 3:
            big = -(2 ** 32)
            for num in nums:
                if num > big:
                    big = num
            return big
        
        for i in range(3):
            highest = -(2 ** 32)
            index = 0
            for j, num in enumerate(nums):
                if num > highest:
                    highest = num
                    index = j

            if i == 2:
                return highest

            nums[index] = nums[-1]
            nums.pop()


    def thirdMaxCleanLinearTime(self, nums: List[int]) -> int:
        first = -(2 ** 32)
        second = -(2 ** 32)
        third = -(2 ** 32)

        for num in nums:
            # Can also extract the equality check like this:
            # if num == first or num == second or num == third:
            #   continue
            
            if num > first and num != first:
                third = second
                second = first
                first = num

            elif num > second and num != first:
                third = second
                second = num

            elif num > third and num != first and num != second:
                third = num

        if third > -(2 ** 32):
            return third
        
        return first