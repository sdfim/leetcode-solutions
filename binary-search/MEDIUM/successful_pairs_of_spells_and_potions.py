# Successful Pairs of Spells and Potions
# Problem: https://leetcode.com/problems/successful-pairs-of-spells-and-potions/

from typing import List
import bisect

class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        m = len(potions)
        ans = []
        
        for s in spells:
            # Need s * p >= success => p >= ceil(success / s)
            min_p = (success + s - 1) // s
            idx = bisect.bisect_left(potions, min_p)
            count = m - idx
            ans.append(count)
            
        return ans

if __name__ == "__main__":
    solution = Solution()
    print(solution.successfulPairs([5,1,3], [1,2,3,4,5], 7)) # [4,0,3]
