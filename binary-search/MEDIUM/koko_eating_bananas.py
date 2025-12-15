# Koko Eating Bananas
# Problem: https://leetcode.com/problems/koko-eating-bananas/

from typing import List
import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # Binary search on the speed k
        # k ranges from 1 to max(piles)
        
        left, right = 1, max(piles)
        res = right
        
        while left <= right:
            k = (left + right) // 2
            
            # Calculate hours needed
            hours = 0
            for p in piles:
                hours += math.ceil(p / k)
                
            if hours <= h:
                res = k
                right = k - 1
            else:
                left = k + 1
                
        return res

if __name__ == "__main__":
    solution = Solution()
    print(solution.minEatingSpeed([3,6,7,11], 8))  # Output: 4
