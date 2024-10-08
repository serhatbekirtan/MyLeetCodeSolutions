from typing import List


class Solution:
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        cache = {}

        def recursive(i):
            if i == len(books):
                return 0
            if i in cache:
                return cache[i]
        
            cur_width = shelfWidth
            max_height = 0
            cache[i] = float("inf")

            for j in range(i, len(books)):
                width, height = books[j]
                
                if cur_width < width:
                    break

                cur_width -= width
                max_height = max(max_height, height)
                cache[i] = min(cache[i], recursive(j + 1) + max_height)

            return cache[i]
        
        return recursive(0)
    

    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        dp = [0] * (len(books) + 1)

        for i in range(len(books) - 1, -1, -1):
            cur_width = shelfWidth
            max_height = 0
            dp[i] = float("inf")
                
            for j in range(i, len(books)):
                width, height = books[j]
                
                if cur_width < width:
                    break

                cur_width -= width
                max_height = max(max_height, height)
                dp[i] = min(dp[i], dp[j + 1] + max_height)
            
        return dp[0]
