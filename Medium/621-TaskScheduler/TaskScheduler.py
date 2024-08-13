import heapq
from collections import Counter, deque
from typing import List


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        time = 0
        heap = [-val for val in Counter(tasks).values()]
        heapq.heapify(heap)
        queue = deque()

        while heap or queue:
            time += 1

            if heap:
                count = heapq.heappop(heap)
                if count + 1:
                    queue.append([count + 1, time + n])

            if queue and queue[0][1] == time:
                cnt, _ = queue.popleft()
                if cnt:
                    heapq.heappush(heap, cnt)

        return time