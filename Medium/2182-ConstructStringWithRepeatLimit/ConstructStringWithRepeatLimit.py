import heapq
from typing import Counter


class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        freq = Counter(s)

        maxHeap = [(-ord(char), count) for char, count in freq.items()]
        heapq.heapify(maxHeap)

        res = []

        while maxHeap:
            char, count = heapq.heappop(maxHeap)
            char = chr(-char)
            currCount = min(count, repeatLimit)
            res.append(char * currCount)

            if count - currCount > 0 and maxHeap:
                char2, count2 = heapq.heappop(maxHeap)
                char2 = chr(-char)
                res.append(char2)

                if count2 > 1:
                    heapq.heappush(maxHeap, (-ord(char2), count2 - 1))
                heapq.heappush(maxHeap, (-ord(char), count - currCount))

        return "".join(res)