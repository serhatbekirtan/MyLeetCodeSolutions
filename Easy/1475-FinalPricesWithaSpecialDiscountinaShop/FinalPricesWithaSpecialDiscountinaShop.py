from typing import List


class Solution:
    # Brute Force Solution.
    def finalPrices(self, prices: List[int]) -> List[int]:
        res = []

        for i in range(len(prices)):
            price = prices[i]
            discount = 0

            for j in range(i + 1, len(prices)):
                if prices[j] <= price:
                    discount = prices[j]
                    break
            
            finalPrice = price - discount
            res.append(finalPrice)

        return res
    
    # Monotonic Stack Solution.
    def finalPrices(self, prices: List[int]) -> List[int]:
        res = [p for p in prices]

        stack = []

        for i in range(len(prices)):
            while stack and prices[stack[-1]] >= prices[i]:
                j = stack.pop()
                res[j] -= prices[i]

            stack.append(i)

        return res