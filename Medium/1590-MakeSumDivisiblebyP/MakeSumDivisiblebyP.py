from typing import List


class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        total = sum(nums)
        remainder = total % p
        n = len(nums)

        if remainder == 0:
            return 0
        
        res = n
        remainderMap = {0: -1}
        currSum = 0

        for i, num in enumerate(nums):
            currSum = (currSum + num) % p
            prefix = (currSum - remainder) % p

            if prefix in remainderMap:
                length = i - remainderMap[prefix]
                res = min(res, length)

            remainderMap[currSum] = i

        return res if res != n else -1