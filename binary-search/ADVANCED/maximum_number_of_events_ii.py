# Maximum Number of Events That Can Be Attended II
# Problem: https://leetcode.com/problems/maximum-number-of-events-that-can-be-attended-ii/

from typing import List
import bisect
import functools

class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        # events: [start, end, value]
        # Sort by start time
        events.sort()
        n = len(events)
        
        # Starts array for binary search
        starts = [e[0] for e in events]
        
        @functools.lru_cache(None)
        def solve(idx, count):
            if count == 0 or idx == n:
                return 0
            
            # Option 1: Skip current event
            res = solve(idx + 1, count)
            
            # Option 2: Take current event
            # Find next event that starts after current event ends
            next_idx = bisect.bisect_right(starts, events[idx][1])
            res = max(res, events[idx][2] + solve(next_idx, count - 1))
            
            return res
            
        return solve(0, k)

if __name__ == "__main__":
    solution = Solution()
    print(solution.maxValue([[1,2,4],[3,4,3],[2,3,1]], 2)) # Output: 7
