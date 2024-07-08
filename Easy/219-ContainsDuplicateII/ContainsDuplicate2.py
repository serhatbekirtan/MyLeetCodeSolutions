from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hashmap = {}
        
        i = 0

        while i < len(nums):
            index = hashmap.get(nums[i])
            
            if index is not None:
                if abs(index - i) <= k:
                    return True
                
                hashmap[nums[i]] = i
                i += 1
                continue
            
            hashmap[nums[i]] = i
            i += 1

        return False
    

    def containsNearbyDuplicateSlidingWindow(self, nums: List[int], k: int) -> bool:
        window = set()
        L = 0

        for R in range(len(nums)):
            if R - L > k:
                window.remove(nums[L])
                L += 1
                
            if nums[R] in window:
                return True
            
            window.add(nums[R])

        return False