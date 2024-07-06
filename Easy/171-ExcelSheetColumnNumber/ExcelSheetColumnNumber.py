class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        columnNumber = 0
        power = 0

        while columnTitle:
            character = columnTitle[-1]
            columnTitle = columnTitle[:-1]
            
            columnNumber_Character = ord(character) - 64
            columnNumber += pow(26, power) * columnNumber_Character

            power += 1

        return columnNumber