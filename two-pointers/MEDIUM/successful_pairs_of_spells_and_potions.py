# Successful Pairs of Spells and Potions
# Problem: https://leetcode.com/problems/successful-pairs-of-spells-and-potions/
# Solution:

from typing import List
import bisect

class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        res = []
        m = len(potions)
        
        for spell in spells:
            cutoff = (success + spell - 1) // spell
            idx = bisect.bisect_left(potions, cutoff)
            res.append(m - idx)
            
        return res

if __name__ == "__main__":
    solution = Solution()
    
    spells = [5,1,3]
    potions = [1,2,3,4,5]
    success = 7
    print(f"Successful pairs: {solution.successfulPairs(spells, potions, success)}")
