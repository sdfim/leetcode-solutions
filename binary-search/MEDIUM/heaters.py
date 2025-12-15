# Heaters
# Problem: https://leetcode.com/problems/heaters/

from typing import List
import bisect

class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        heaters.sort()
        radius = 0
        
        for house in houses:
            # Find insertion point
            idx = bisect.bisect_left(heaters, house)
            
            dist1 = float('inf')
            dist2 = float('inf')
            
            if idx < len(heaters):
                dist1 = heaters[idx] - house
            if idx > 0:
                dist2 = house - heaters[idx - 1]
                
            radius = max(radius, min(dist1, dist2))
            
        return radius

if __name__ == "__main__":
    solution = Solution()
    print(solution.findRadius([1,2,3], [2]))  # Output: 1
