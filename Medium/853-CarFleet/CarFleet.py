from typing import List


class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = []
        stack = []

        for pos, velo in zip(position, speed):
            cars.append([pos, velo])

        cars = sorted(cars)
        for p, v in reversed(cars):
            stack.append((target - p) / v)
            
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        
        return len(stack)