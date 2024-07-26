from collections import defaultdict
import heapq
from typing import List


class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        adjacencyList = defaultdict(list)

        for v1, v2, weight in edges:
            adjacencyList[v1].append((v2, weight))
            adjacencyList[v2].append((v1, weight))

        def dijkstra(src):
            heap = [(0, src)] # weight, src
            visit = set()

            while heap:
                distance, node = heapq.heappop(heap)

                if node in visit:
                    continue

                visit.add(node)

                for neighbor, weight in adjacencyList[node]:
                    neighbor_distance = distance + weight
                    if neighbor_distance <= distanceThreshold:
                        heapq.heappush(heap, (neighbor_distance, neighbor))

            return len(visit) - 1
        
        res , min_count = -1, n
        for src in range(n):
            count = dijkstra(src)
            if count <= min_count:
                res, min_count = src, count

        return res