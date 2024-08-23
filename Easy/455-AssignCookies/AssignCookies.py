from typing import List


class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort(), s.sort()

        res, cookie, greed = 0, 0, 0

        while cookie < len(s) and greed < len(g):
            if s[cookie] >= g[greed]:
                res += 1
                greed += 1

            cookie += 1

        return res
    

    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort(), s.sort()
        greed = 0

        for cookie in s:
            if cookie >= g[greed]:
                greed += 1
            if greed == len(g):
                break

        return greed