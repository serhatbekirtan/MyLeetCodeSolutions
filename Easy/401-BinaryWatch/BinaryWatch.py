from typing import List


class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        result = []

        for h in range(12):
            for m in range(60):
                h_ones= bin(h).count('1')
                m_ones = bin(m).count('1')
                if h_ones + m_ones == turnedOn:
                    result.append(f"{h}:{m:02}")
        
        return result
    
    # Hour is: 1, binary hour is: 0b1
    # Minute is: 3, binary minute is: 0b11
    # Read is (Hour + Minute) = 0b10b11
    # ['1:03']