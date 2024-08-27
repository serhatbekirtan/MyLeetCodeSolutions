from collections import defaultdict
import heapq
from typing import List


class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        p, g = [0.0] * n, defaultdict(list)
        for index, (a, b) in enumerate(edges):
            g[a].append((b, index))
            g[b].append((a, index))

        p[start_node] = 1.0
        heap = [(-p[start_node], start_node)]    
        while heap:
            prob, cur = heapq.heappop(heap)
            if cur == end_node:
                return -prob

            for neighbor, index in g.get(cur, []):
                if -prob * succProb[index] > p[neighbor]:
                    p[neighbor] = -prob * succProb[index]
                    heapq.heappush(heap, (-p[neighbor], neighbor))
                    
        return 0.0