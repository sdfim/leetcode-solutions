# Avoid Flood in The City
# Problem: https://leetcode.com/problems/avoid-flood-in-the-city/

from typing import List
import bisect

class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        # Map lake_id -> last_rain_day
        full_lakes = {}
        # List of available dry days
        dry_days = []
        ans = [-1] * len(rains)
        
        for i, lake in enumerate(rains):
            if lake == 0:
                dry_days.append(i)
                ans[i] = 1 # Default, can change later
            else:
                if lake in full_lakes:
                    # Lake is full, need to empty it before today but after it was filled
                    last_filled = full_lakes[lake]
                    # Find a dry day > last_filled
                    idx = bisect.bisect_right(dry_days, last_filled)
                    
                    if idx < len(dry_days):
                        day_to_dry = dry_days.pop(idx)
                        ans[day_to_dry] = lake
                    else:
                        return []
                full_lakes[lake] = i
                ans[i] = -1
                
        return ans

if __name__ == "__main__":
    solution = Solution()
    print(solution.avoidFlood([1,2,3,4]))  # Output: [-1,-1,-1,-1]
    print(solution.avoidFlood([1,2,0,0,2,1]))  # Output: [-1,-1,2,1,-1,-1]
