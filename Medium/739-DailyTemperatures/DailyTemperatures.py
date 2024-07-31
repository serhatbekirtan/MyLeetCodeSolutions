from typing import List


class Solution:
    # O(n^2), Brute Force.
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = []

        for i, temp in enumerate(temperatures):
            days = 0
            result.append(days)

            while i + days < len(temperatures):
                if temperatures[i + days] <= temp:
                    days += 1
                else:
                    result[i] += days
                    break

        return result
    

    # O(n) Time, O(n) Space.
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = []

        for i, temp in enumerate(temperatures):

            while stack and temp > stack[-1][1]:
                colderIndex, colderTemp = stack.pop()
                result[colderIndex] = i - colderIndex
                
            stack.append([i, temp])

        return result