from collections import defaultdict
from typing import List


class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        x_dict = defaultdict(list)
        y_dict = defaultdict(list)
        points = {(i,j) for i,j in stones}

        def dfs(a,b):
            points.discard((a,b))
            for y in x_dict[a]:
                if (a,y) in points:
                    dfs(a,y)

            for x in y_dict[b]:
                if (x,b) in points:
                    dfs(x,b)

        for i,j in stones:
            x_dict[i].append(j)
            y_dict[j].append(i)

        count = 0
        for a,b in stones:
            if (a,b) in points:
                dfs(a,b)
                count += 1

        return len(stones) - count
    

# Union Find Solution
class Solution:
    def removeStones(self, stones):
        uf = self.UnionFind(20002)

        for x, y in stones:
            uf._union_nodes(x, y + 10001)

        return len(stones) - uf.component_count


    class UnionFind:
        def __init__(self, n):
            self.parent = [-1] * n
            self.component_count = (0)
            self.unique_nodes = (set())

        def _find(self, node):
            if node not in self.unique_nodes:
                self.component_count += 1
                self.unique_nodes.add(node)

            if self.parent[node] == -1:
                return node

            self.parent[node] = self._find(self.parent[node])
            return self.parent[node]

        def _union_nodes(self, node1, node2):
            root1 = self._find(node1)
            root2 = self._find(node2)

            if root1 == root2:
                return

            self.parent[root1] = root2
            self.component_count -= 1