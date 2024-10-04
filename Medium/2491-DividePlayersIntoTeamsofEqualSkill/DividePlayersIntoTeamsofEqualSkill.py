from typing import Counter, List


class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        n = len(skill)

        if n % 2:
            return -1
            
        teamSkillPoint = sum(skill) // (n // 2)
        freqs = Counter(skill)
        res = 0

        for point in skill:
            complement = teamSkillPoint - point
            if not freqs[point] and not freqs[complement]:
                continue
            elif freqs[point] and freqs[complement]:
                freqs[point] -= 1
                freqs[complement] -= 1
                res += (point * complement)
            else:
                return -1
        
        return res