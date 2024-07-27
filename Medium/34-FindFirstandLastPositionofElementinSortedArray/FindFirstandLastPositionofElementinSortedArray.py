from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        def binarySearch(first):
            L = 0
            R = len(nums) - 1
            index = -1

            while L <= R:
                mid = (L + R) // 2

                if nums[mid] > target:
                    R = mid - 1
                elif nums[mid] < target:
                    L = mid + 1
                else:
                    index = mid
                    if first:
                        R = mid - 1
                    else:
                        L = mid + 1
            
            return index
        
        first = binarySearch(True)
        last = binarySearch(False)

        return [first, last]