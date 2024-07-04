class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        result = ""

        while columnNumber >= 1:
            mod = columnNumber % 26

            if mod == 0:
                mod = 26
                columnNumber -= 26

            result += chr(mod + 64)
            columnNumber = columnNumber // 26

        return result[::-1]

    
    def convertToTitleNeetCode(self, columnNumber: int) -> str:
        res = ""

        while columnNumber > 0:
            offset = (columnNumber - 1) % 26
            res += chr(ord('A') + offset)
            columnNumber = (columnNumber - 1) // 26

        return res[::-1]