# Divide Players Into Teams of Equal Skill
# Problem: https://leetcode.com/problems/divide-players-into-teams-of-equal-skill/
# Solution:

from typing import List

class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        l, r = 0, len(skill) - 1
        target = skill[l] + skill[r]
        res = 0
        
        while l < r:
            if skill[l] + skill[r] != target:
                return -1
            res += skill[l] * skill[r]
            l += 1
            r -= 1
            
        return res

if __name__ == "__main__":
    solution = Solution()
    
    skill1 = [3,2,5,1,3,4]
    print(f"Chemistry sum of {skill1}: {solution.dividePlayers(skill1)}")
    
    skill2 = [1,1,2,3]
    print(f"Chemistry sum of {skill2}: {solution.dividePlayers(skill2)}")
