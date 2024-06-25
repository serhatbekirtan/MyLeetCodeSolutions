from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        while m > 0 and n > 0:
            j = m + n - 1
            if nums1[m - 1] < nums2[n - 1]:
                nums1[j] = nums2[n - 1]
                n = n - 1
            else:
                nums1[j] = nums1[m - 1]
                m = m - 1

        while n > 0:
            j = m + n - 1
            nums1[j] = nums2[n - 1]
            n = n - 1