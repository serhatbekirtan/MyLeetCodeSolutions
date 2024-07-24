from typing import List


class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        # result = []
        mapArray = []

        for num in nums:
            current = ""
            realNum = num

            while num >= 0:
                digit = num % 10
                num = num // 10
                mapDigit = mapping[digit]
                current += str(mapDigit)
                if num == 0:
                    break

            current = current[::-1]
            mapArray.append([realNum, int(current)])

        mapArray = sorted(mapArray, key=lambda x: x[1])

        # Use List comprehension instead.
        # for p in mapArray:
        #     result.append(p[0])
        
        return [p[0] for p in mapArray]
    

    def sortJumbledClean(self, mapping: List[int], nums: List[int]) -> List[int]:
        pairs = []

        for i, num in enumerate(nums):
            num = str(num)
            current = ""

            for digit in num:
                current += str(mapping[int(digit)])

            pairs.append((int(current), i))

        pairs.sort()
        return [nums[p[1]] for p in pairs]