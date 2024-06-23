class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        if len(s) == 0:
            return 0

        i = len(s) - 1
        last_word = ""

        while i >= 0:
            if s[i] == " ":
                i -= 1
            else:
                while True:
                    if i < 0:
                        return len(last_word)

                    if s[i] == " ":
                        return len(last_word)
                    
                    last_word += s[i]
                    i -= 1

        return 0


    def lengthOfLastWord2(self, s: str) -> int:

        stripped = s.strip()

        if len(stripped) == 0:
            return 0

        i = len(stripped) - 1
        last_word_count = 0

        while i >= 0:
            last_word_count += 1
            i -= 1

            if i < 0:
                return last_word_count

            if stripped[i] == " ":
                return last_word_count


    def lengthOfLastWord3(self, s: str) -> int:

        counter = 0
        i = len(s) - 1

        while s[i] == " ":
            i -= 1
        
        while i >= 0 and s[i] != " ":
            counter += 1
            i -= 1

        return counter