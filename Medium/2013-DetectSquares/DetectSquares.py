from collections import defaultdict
from typing import List


class DetectSquares:

    def __init__(self):
        self.points = defaultdict(int)
        self.pts = []

    def add(self, point: List[int]) -> None:
        self.points[(point[0], point[1])] += 1
        self.pts.append(point)

    def count(self, point: List[int]) -> int:
        res = 0
        px, py = point
        
        for x, y in self.pts:
            if (abs(px - x) != abs(py - y)) or px == x or py == y:
                continue
            res += self.points[(x, py)] * self.points[(px, y)]

        return res
    

class DetectSquares:

    def __init__(self):
        self.points = defaultdict(int)

    def add(self, point: List[int]) -> None:
        self.points[(point[0], point[1])] += 1

    def count(self, point: List[int]) -> int:
        res = 0
        px, py = point
        
        for (x, y), n in self.points.items():
            if (abs(px - x) == abs(py - y)) and px != x and (x, py) in self.points and (px, y) in self.points:
                res += n * self.points[(x, py)] * self.points[(px, y)]

        return res