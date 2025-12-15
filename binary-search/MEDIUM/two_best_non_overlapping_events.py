# Two Best Non-Overlapping Events
# Problem: https://leetcode.com/problems/two-best-non-overlapping-events/

from typing import List
import bisect

class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        # Sort by start time
        events.sort()
        n = len(events)
        
        # Precompute max value in suffix [i:]
        max_suffix = [0] * n
        max_suffix[n-1] = events[n-1][2]
        for i in range(n - 2, -1, -1):
            max_suffix[i] = max(max_suffix[i+1], events[i][2])
            
        ans = 0
        start_times = [e[0] for e in events]
        
        for i in range(n):
            s, e, v = events[i]
            # Ans if we take only this event
            ans = max(ans, v)
            
            # Try to take a second event
            # Must start > e
            idx = bisect.bisect_right(start_times, e)
            if idx < n:
                ans = max(ans, v + max_suffix[idx])
                
        return ans

if __name__ == "__main__":
    solution = Solution()
    print(solution.maxTwoEvents([[1,3,2],[4,5,2],[2,4,3]])) # 4
