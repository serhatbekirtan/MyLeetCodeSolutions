from typing import List


class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.sums = [0]

        for i, num in enumerate(nums):
            self.sums.append(num + self.sums[i])


    def sumRange(self, left: int, right: int) -> int:
        return self.sums[right + 1] - self.sums[left]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)