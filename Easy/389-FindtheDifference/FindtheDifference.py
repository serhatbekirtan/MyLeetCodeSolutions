from typing import Counter


class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        hashmap = Counter(s)

        for char in t:
            if hashmap.get(char, 0) > 0:
                hashmap[char] -= 1
            else:
                return char
            
    
    # ASCII solution using ascii values of characters.
    def findTheDifferenceASCII(self, s: str, t: str) -> str:
        ord_sum = 0

        for char in t:
            ord_sum += ord(char)

        for char in s:
            ord_sum -= ord(char)

        return chr(ord_sum)
    

    # Solution by sorting the strings.
    def findTheDifference(self, s: str, t: str) -> str:
        s = sorted(s)
        t = sorted(t)

        for i in range(len(s)):
            if s[i] != t[i]:
                return t[i]

        return t[-1]