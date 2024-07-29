from typing import List


class Solution:
    # Brute Force
    def numTeams(self, rating: List[int]) -> int:
        result = []

        for i in range(len(rating) - 2):
            tempInc = []
            tempInc.append(rating[i])
            tempDec = []
            tempDec.append(rating[i])

            for j in range(i + 1, len(rating) - 1):
                if tempInc[0] < rating[j]:
                    tempInc.append(rating[j])
                else:
                    tempDec.append(rating[j])

                for k in range(j + 1, len(rating)):
                    if len(tempInc) == 2 and tempInc[-1] < rating[k]:
                        tempInc.append(rating[k])
                    if len(tempDec) == 2 and tempDec[-1] > rating[k]:
                        tempDec.append(rating[k])

                    if len(tempInc) == 3:
                        result.append(tempInc)
                        tempInc.pop()
                    if len(tempDec) == 3:
                        result.append(tempDec)
                        tempDec.pop()
                
                if len(tempInc) == 2:
                    tempInc.pop()
                if len(tempDec) == 2:
                    tempDec.pop()

        return len(result)
    

    # Smarter way, count smaller left greater right and vice versa.
    def numTeamsLin(self, rating: List[int]) -> int:
        result = 0

        for mid in range(1, len(rating) - 1):
            smallerLeft, smallerRight, greaterLeft, greaterRight = 0, 0, 0, 0
            
            for L in range(mid):
                if rating[L] < rating[mid]:
                    smallerLeft += 1
                else:
                    greaterLeft += 1
            
            for R in range(mid + 1, len(rating)):
                if rating[R] < rating[mid]:
                    smallerRight += 1
                else:
                    greaterRight += 1
            
            result += (smallerLeft * greaterRight) + (greaterLeft * smallerRight)

        return result