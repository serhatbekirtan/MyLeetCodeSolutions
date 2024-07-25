import heapq
from typing import List


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        heapq.heapify(nums)
        sortedNums = []

        while nums:
            sortedNums.append(heapq.heappop(nums))

        return sortedNums
    

    def sortArray(self, nums: List[int]) -> List[int]:
        
        def mergeSort(arr, L, R):
            if L == R:
                return arr
            
            M = (L + R) // 2

            mergeSort(arr, L, M)
            mergeSort(arr, M + 1, R)
            merge(arr, L, M, R)

            return arr

        
        def merge(arr, L, M, R):
            leftArray = arr[L : M + 1]
            rightArray = arr[M + 1 : R + 1]

            i, j = 0, 0
            k = L

            while i < len(leftArray) and j < len(rightArray):
                if leftArray[i] <= rightArray[j]:
                    arr[k] = leftArray[i]
                    i += 1
                else:
                    arr[k] = rightArray[j]
                    j += 1
                k += 1
                
            while i < len(leftArray):
                arr[k] = leftArray[i]
                i += 1
                k += 1
            
            while j < len(rightArray):
                arr[k] = rightArray[j]
                j += 1
                k += 1


        return mergeSort(nums, 0, len(nums) - 1)