from functools import cmp_to_key
from typing import List


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        num_strings = [str(num) for num in nums]
        num_strings.sort(key=lambda a: a * 10, reverse=True)

        return str(int("".join(num_strings)))
    

    def largestNumber(self, nums: List[int]) -> str:
        num_strings = [str(num) for num in nums]

        def compare(x, y):
            return -1 if x + y > y + x else 1

        num_strings.sort(key=cmp_to_key(compare))

        return str(int("".join(num_strings)))