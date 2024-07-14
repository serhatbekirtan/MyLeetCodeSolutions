from typing import Counter, List


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hashmap = Counter(nums1)
        result = []

        for num in nums2:
            if hashmap[num] > 0:
                result.append(num)
                hashmap[num] -= 1
                    
        return result
    
    # Solution if the given arrays are in ascending order.
    def intersectSorted(self, nums1: List[int], nums2: List[int]) -> List[int]:
        i = 0
        j = 0
        result = []
        
        while i < len(nums1) and j < len(nums2):
            if nums1[i] == nums2[j]:
                result.append(nums1[i])
                i += 1
                j += 1

            elif nums1[i] < nums2[j]:
                i += 1

            else:
                j += 1

        return result