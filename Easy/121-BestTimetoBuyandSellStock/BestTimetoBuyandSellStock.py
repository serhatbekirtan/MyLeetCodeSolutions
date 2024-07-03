from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0

        min_buy = prices[0]

        for i in range(len(prices)):
            if prices[i] < min_buy:
                min_buy = prices[i]
            
            profit = prices[i] - min_buy

            if profit > max_profit:
                max_profit = profit

        return max_profit