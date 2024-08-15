from typing import List


class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        fiveDollar = 0
        tenDollar = 0

        for bill in bills:
            if bill == 5:
                fiveDollar += 1

            elif bill == 10:
                if not fiveDollar:
                    return False
                tenDollar += 1
                fiveDollar -= 1
                
            else:
                if tenDollar and fiveDollar:
                    tenDollar -= 1
                    fiveDollar -= 1
                elif fiveDollar >= 3:
                    fiveDollar -= 3
                else:
                    return False
        
        return True