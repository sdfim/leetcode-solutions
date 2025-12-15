# Heaters
# Problem: https://leetcode.com/problems/heaters/
# Solution:

from typing import List
import bisect

class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort()
        heaters.sort()
        radius = 0
        
        for house in houses:
            # Find closest heater
            idx = bisect.bisect_left(heaters, house)
            
            dist1 = float('inf')
            if idx < len(heaters):
                dist1 = heaters[idx] - house
            
            dist2 = float('inf')
            if idx > 0:
                dist2 = house - heaters[idx-1]
                
            radius = max(radius, min(dist1, dist2))
            
        return radius

if __name__ == "__main__":
    solution = Solution()
    
    houses1 = [1,2,3]
    heaters1 = [2]
    print(f"Radius for houses {houses1}, heaters {heaters1}: {solution.findRadius(houses1, heaters1)}")
    
    houses2 = [1,2,3,4]
    heaters2 = [1,4]
    print(f"Radius for houses {houses2}, heaters {heaters2}: {solution.findRadius(houses2, heaters2)}")
