class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        map = {}
        arr_s = []
        word = ""
        result = ""

        for char in s:
            if char == " ":
                arr_s.append(word)
                word = ""
            else:
                word += char

        arr_s.append(word)

        if len(pattern) != len(arr_s):
            return False

        i = 0
        for c in pattern:
            if arr_s[i] not in map.values():
                map[c] = arr_s[i]
            i += 1

        for char in pattern:
            if char not in map:
                return False
            result += map[char]

        clean_s = s.replace(" ", "")

        return result == clean_s
    

    def wordPatternNeetCode(self, pattern: str, s: str) -> bool:
        words = s.split(" ")
        if len(pattern) != len(words):
            return False
        
        charToWord = {}
        wordToChar = {}

        for char, word in zip(pattern, words):
            if char in charToWord and charToWord[char] != word:
                return False
            if word in wordToChar and wordToChar[word] != char:
                return False
            
            charToWord[char] = word
            wordToChar[word] = char

        return True