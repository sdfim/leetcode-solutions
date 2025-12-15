# Minimum Time to Complete All Deliveries
# Problem: https://leetcode.com/problems/minimum-time-to-complete-all-deliveries/

from typing import List
import math

class Solution:
    def minTime(self, d: List[int], r: List[int]) -> int:
        d1, d2 = d
        r1, r2 = r
        lcm_r = math.lcm(r1, r2)
        
        def check(t):
            # Slots available
            s1 = t - t // r1
            s2 = t - t // r2
            s_all = t - t // lcm_r
            
            # Check individual sufficiency
            # Drone 1 can do at most s1
            # Drone 2 can do at most s2
            # Together they can do s_all tasks (since s_all counts slots where >=1 drone is active).
            # Wait. "Only one drone can make a delivery at any given hour".
            # So total deliveries <= total hours where at least one drone is active.
            # Total active hours = T - (hours where both inactive).
            # Both inactive when both recharging (multiples of LCM).
            # So s_all is indeed the capacity of the system.
            
            return s1 >= d1 and s2 >= d2 and s_all >= d1 + d2
            
        left, right = 1, 10**18
        ans = right
        
        while left <= right:
            mid = (left + right) // 2
            if check(mid):
                ans = mid
                right = mid - 1
            else:
                left = mid + 1
        return ans

if __name__ == "__main__":
    solution = Solution()
    print(solution.minTime([3,2], [2,3])) # Example inputs
