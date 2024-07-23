from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        result = 0

        i = 0
        j = len(height) - 1

        while i < j:
            x = j - i
            y = min(height[i], height[j])
            
            result = max(result, x * y)

            if height[i] < height[j]:
                i += 1
            else:
                j -= 1

        return result