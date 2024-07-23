from typing import Counter, List


class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        frequencies = Counter(nums)

        arr = []
        for key in frequencies:
            arr.append([key, frequencies[key]])

        arr = sorted(arr, key=lambda x: x[0], reverse=True)
        arr = sorted(arr, key=lambda x: x[-1])

        result = []
        for array in arr:
            for i in range(array[1]):
                result.append(array[0])

        return result
    

    def frequencySort(self, nums: List[int]) -> List[int]:
        frequency = Counter(nums)

        nums = sorted(nums, key=lambda x: (frequency[x], -x))

        return nums