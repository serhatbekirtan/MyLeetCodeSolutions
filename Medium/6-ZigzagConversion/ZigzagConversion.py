class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if len(s) <= numRows:
            return s
        
        result = []

        for r in range(numRows):
            incrementer = 2 * (numRows - 1)
            for i in range(r, len(s), incrementer):
                result.append(s[i])
                if(r > 0 and r < numRows - 1 and i + incrementer - 2 * r < len(s)):
                    result.append(s[i + incrementer - 2 * r])

        return "".join(result)
    

    # A Brilliant Solution.
    def convertClean(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
            
        rowArr = [""] * numRows
        rowIndex = 1
        goUpFlag = True

        for char in s:
            rowArr[rowIndex - 1] += char

            if rowIndex == numRows:
                goUpFlag = False

            elif rowIndex == 1:
                goUpFlag = True
            
            if goUpFlag:
                rowIndex += 1
            else:
                rowIndex -= 1
        
        return "".join(rowArr)