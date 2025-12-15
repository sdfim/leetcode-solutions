# Minimum Speed to Arrive on Time
# Problem: https://leetcode.com/problems/minimum-speed-to-arrive-on-time/

from typing import List
import math

class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        n = len(dist)
        if hour <= n - 1:
            return -1
            
        def time_taken(speed):
            total = 0
            for i in range(n - 1):
                total += math.ceil(dist[i] / speed)
            total += dist[-1] / speed # Last one doesn't wait
            return total
            
        left, right = 1, 10**7
        res = -1
        
        while left <= right:
            mid = (left + right) // 2
            if time_taken(mid) <= hour:
                res = mid
                right = mid - 1
            else:
                left = mid + 1
                
        return res

if __name__ == "__main__":
    solution = Solution()
    print(solution.minSpeedOnTime([1,3,2], 6))  # Output: 1
    print(solution.minSpeedOnTime([1,3,2], 2.7)) # Output: 3
