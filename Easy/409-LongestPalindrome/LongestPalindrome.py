from typing import Counter


class Solution:
    def longestPalindrome(self, s: str) -> int:
        hashmap = Counter(s)
        longest = 0
        biggest_odd = 0

        for key in hashmap:
            value = hashmap[key]

            if value % 2 == 0:
                longest += value
                continue
            
            if value > biggest_odd:
                if biggest_odd: 
                    longest += (biggest_odd - 1)
                biggest_odd = value
            else:
                longest += (value - 1)

        return (longest + biggest_odd)
    

    def longestPalindromeClean(self, s: str) -> int:
        seen = set()
        result = 0

        for char in s:
            if char in seen:
                seen.remove(char)
                result += 2
            else:
                seen.add(char)

        if seen:
            result += 1

        return result