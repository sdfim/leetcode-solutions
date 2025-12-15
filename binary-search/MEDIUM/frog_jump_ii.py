# Frog Jump II
# Problem: https://leetcode.com/problems/frog-jump-ii/

from typing import List

class Solution:
    def maxJump(self, stones: List[int]) -> int:
        # Greedy strategy:
        # Go 0 -> 2 -> 4 ... -> N
        # Return N -> N-1 -> ... -> 1 -> 0 (filling gaps)
        # Actually to minimize max jump, we alternate stones.
        # Stones sorted.
        # Max jump is max(stones[i+2] - stones[i]).
        # And check first step stones[1]-stones[0] / last step?
        # Specifically: max(stones[1]-stones[0], stones[2]-stones[0], stones[3]-stones[1]...)
        
        if len(stones) == 2:
            return stones[1] - stones[0]
            
        res = 0
        # Optimal path uses indices 0, 2, 4... going up
        # And 1, 3, 5... coming down (or vice versa).
        # We process step size 2.
        
        for i in range(len(stones) - 2):
            res = max(res, stones[i+2] - stones[i])
            
        return res

if __name__ == "__main__":
    solution = Solution()
    print(solution.maxJump([0,2,5,6,7])) # 5
