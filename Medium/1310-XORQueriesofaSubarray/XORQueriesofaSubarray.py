from typing import List


class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        res = []
        prefix = [0]
        
        for val in arr:
            prefix.append(prefix[-1] ^ val)

        for left, right in queries:
            res.append(prefix[right + 1] ^ prefix[left])

        return res
    

    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        res = []
        
        for i in range(1, len(arr)):
            arr[i] = arr[i - 1] ^ arr[i]

        for left, right in queries:
            res.append(arr[right] if left == 0 else arr[right] ^ arr[left - 1])

        return res