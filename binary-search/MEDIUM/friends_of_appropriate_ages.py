# Friends Of Appropriate Ages
# Problem: https://leetcode.com/problems/friends-of-appropriate-ages/

from typing import List
import bisect

class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        ages.sort()
        count = 0
        n = len(ages)
        
        for i, age in enumerate(ages):
            # Conditions:
            # 1. age[y] <= 0.5 * age[x] + 7  --> age[y] > 0.5 * age[x] + 7
            # 2. age[y] > age[x]
            # 3. age[y] > 100 and age[x] < 100 (Redundant usually)
            
            # We want friends y such that:
            # y <= x (from condition 2, except same age can friend)
            # y > 0.5 * x + 7
            
            lowest = 0.5 * age + 7
            if lowest >= age: continue
            
            # Find range (lowest, age]
            # y > lowest
            left_idx = bisect.bisect_right(ages, lowest)
            
            # y <= age
            right_idx = bisect.bisect_right(ages, age) - 1
            
            if right_idx >= left_idx:
                count += (right_idx - left_idx + 1)
                # Exclude self
                count -= 1
                
        return count

if __name__ == "__main__":
    solution = Solution()
    print(solution.numFriendRequests([16,16]))  # Output: 2
    print(solution.numFriendRequests([16,17,18]))  # Output: 2
