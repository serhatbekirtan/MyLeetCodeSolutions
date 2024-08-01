from typing import List


class Solution:
    # O(logm*n) Time, O(1) Space.
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def binarySearch(left, right, arr):
            while left <= right:
                mid = (left + right) // 2
                if arr[mid] > target:
                    right = mid - 1
                elif arr[mid] < target:
                    left = mid + 1
                else:
                    return True
            return False

        L, mid, R = 0, 0, len(matrix) - 1

        while L <= R:
            mid = (L + R) // 2

            if matrix[mid][0] > target:
                R = mid - 1
            elif matrix[mid][-1] < target:
                L = mid + 1
            else:
                break
        
        return binarySearch(0, len(matrix[mid]) - 1, matrix[mid])