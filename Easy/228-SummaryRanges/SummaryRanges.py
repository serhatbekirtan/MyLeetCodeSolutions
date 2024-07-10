from typing import List


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return None

        i = 0
        range_Start = nums[i]
        range_End = 0

        result = []

        while i < len(nums):
            range_End = nums[i]

            if i == len(nums) - 1:
                if range_Start == range_End:
                    result.append(f"{range_Start}")
                    break

                result.append(f"{range_Start}->{range_End}")
                break

            if nums[i + 1] > (nums[i] + 1):
                if range_Start == range_End:
                    result.append(f"{range_Start}")
                    range_Start = nums[i + 1]
                    i += 1
                    continue

                result.append(f"{range_Start}->{range_End}")
                range_Start = nums[i + 1]

            i += 1
        
        return result
    

    def summaryRangesClean(self, nums: List[int]) -> List[str]:
        result = []
        i = 0

        while i < len(nums):
            range_Start = nums[i]

            while i < len(nums) - 1 and (nums[i] + 1) == nums[i + 1]:
                i += 1

            if range_Start == nums[i]:
                result.append(f"{range_Start}")
            else:
                result.append(f"{range_Start}->{nums[i]}")

            i += 1

        return result
