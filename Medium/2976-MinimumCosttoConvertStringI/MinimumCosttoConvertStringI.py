from collections import defaultdict
import heapq
from typing import List


class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        adj = defaultdict(list)
        for src, dst, cur_cost in zip(original, changed, cost):
            adj[src].append((dst, cur_cost))

        def dijkstra(src):
            heap = [(0, src)]
            min_cost_hashmap = {}

            while heap:
                cost, node = heapq.heappop(heap)
                if node in min_cost_hashmap:
                    continue
                min_cost_hashmap[node] = cost
                for neighbor, neighbor_cost in adj[node]:
                    heapq.heappush(heap, (cost + neighbor_cost, neighbor))

            return min_cost_hashmap
        
        # Dict comprehension
        # min_cost_maps = {c:dijkstra(c) for c in set(source)}
        minCostMap = {}
        for char in set(source):
            minCostMap[char] = dijkstra(char)

        result = 0

        for src, dst in zip(source, target):
            if dst not in minCostMap[src]:
                return -1
            result += minCostMap[src][dst]

        return result