# Maximum Number of Groups With Increasing Length
# Problem: https://leetcode.com/problems/maximum-number-of-groups-with-increasing-length/

from typing import List

class Solution:
    def maxIncreasingGroups(self, usageLimits: List[int]) -> int:
        usageLimits.sort()
        total = 0
        groups = 0
        
        for limit in usageLimits:
            total += limit
            # To form 'groups + 1' groups with lengths 1, 2, ..., groups+1:
            # We need sum equal to (groups+1)*(groups+2)/2.
            # If total capacity allows, we can potentially increment groups.
            # A greedy strategy works: with new type of limit 'limit', we add to total.
            # If total >= (groups + 1) * (groups + 2) // 2, we can support one more group.
            # Why? Because we can always distribute the large numbers to the largest groups.
            if total >= (groups + 1) * (groups + 2) // 2:
                groups += 1
                
        return groups

if __name__ == "__main__":
    solution = Solution()
    print(solution.maxIncreasingGroups([1,2,5])) # Output: 3
