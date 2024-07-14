from typing import List


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result1 = set(nums1)
        result2 = set(nums2)
        intersection = result1.intersection(result2)

        return intersection
    

    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result1 = set(nums1)
        result = []

        for num in nums2:
            if num in result1:
                result.append(num)
                result1.remove(num)

        return result