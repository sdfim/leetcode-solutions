# Minimum Time to Complete Trips
# Problem: https://leetcode.com/problems/minimum-time-to-complete-trips/

from typing import List

class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        left, right = 1, min(time) * totalTrips
        res = right
        
        while left <= right:
            mid = (left + right) // 2
            trips = sum(mid // t for t in time)
            if trips >= totalTrips:
                res = mid
                right = mid - 1
            else:
                left = mid + 1
        return res

if __name__ == "__main__":
    solution = Solution()
    print(solution.minimumTime([1,2,3], 5))  # Output: 3
