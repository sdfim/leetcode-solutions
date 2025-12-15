# Minimum Time to Repair Cars
# Problem: https://leetcode.com/problems/minimum-time-to-repair-cars/

from typing import List
import math

class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        # Time for a mechanic to repair n cars is r * n^2.
        # Given time T, mechanic implies r * n^2 <= T => n^2 <= T/r => n <= sqrt(T/r).
        # Total cars = sum(floor(sqrt(T/r))) for all mechanics.
        # We need total >= cars.
        
        # Lower bound time: 1.
        # Upper bound: min(ranks) * cars^2.
        
        min_rank = min(ranks)
        left, right = 1, min_rank * (cars * cars)
        ans = right
        
        while left <= right:
            mid = (left + right) // 2
            total = 0
            for r in ranks:
                total += int(math.isqrt(mid // r))
                
            if total >= cars:
                ans = mid
                right = mid - 1
            else:
                left = mid + 1
        return ans

if __name__ == "__main__":
    solution = Solution()
    print(solution.repairCars([4,2,3,1], 10)) # 16
