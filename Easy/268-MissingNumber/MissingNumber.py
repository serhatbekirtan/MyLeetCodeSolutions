from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        print(nums)

        i = 0
        while i < len(nums):
            if nums[i] != i:
                return i

            i += 1

        return i

    # Linear Time O(n), Constant Space O(1)
    def missingNumber(self, nums: List[int]) -> int:
        total = 0

        for num in nums:
            total += num

        n = len(nums)
        total_nums = (n * (n + 1)) // 2

        return total_nums - total