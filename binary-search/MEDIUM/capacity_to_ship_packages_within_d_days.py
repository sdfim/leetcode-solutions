# Capacity To Ship Packages Within D Days
# Problem: https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/

from typing import List

class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left, right = max(weights), sum(weights)
        res = right
        
        while left <= right:
            cap = (left + right) // 2
            
            # Simulate shipping
            needed_days = 1
            curr_weight = 0
            for w in weights:
                if curr_weight + w > cap:
                    needed_days += 1
                    curr_weight = 0
                curr_weight += w
            
            if needed_days <= days:
                res = cap
                right = cap - 1
            else:
                left = cap + 1
                
        return res

if __name__ == "__main__":
    solution = Solution()
    print(solution.shipWithinDays([1,2,3,4,5,6,7,8,9,10], 5))  # Output: 15
