from typing import List


class Solution:

    def encode(self, strs: List[str]) -> str:
        result = []

        for word in strs:
            encodedWord = str(len(word)) + "#" + word
            result.append(encodedWord)
        
        return "".join(result)


    def decode(self, s: str) -> List[str]:
        digits = "0123456789"
        result = []
        i = 0

        while i < len(s):
                count = ""
                
                while (i < len(s)) and (s[i] in digits) and (s[i] != "#"):
                    count += s[i]
                    i += 1
                
                if count:
                    i += 1
                    count_int = int(count)
                    word = s[i: i + count_int]
                    result.append(word)
                    i += count_int
                
        return result