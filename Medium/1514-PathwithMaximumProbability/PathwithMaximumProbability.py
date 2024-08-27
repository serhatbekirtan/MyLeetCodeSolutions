from collections import defaultdict
import heapq
from typing import List


class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        adj = defaultdict(list)
        for edge, prob in zip(edges, succProb):
            adj[edge[0]].append([edge[1], prob])
            adj[edge[1]].append([edge[0], prob])

        maxHeap = [[-1, start_node]]
        visit = {}

        while maxHeap:
            prob1, node1 = heapq.heappop(maxHeap)
            visit[node1] = -prob1

            if node1 == end_node:
                return -prob1

            for node2, prob2 in adj[node1]:
                if node2 not in visit:
                    heapq.heappush(maxHeap, [-abs(prob1 * prob2), node2])
            
        return 0