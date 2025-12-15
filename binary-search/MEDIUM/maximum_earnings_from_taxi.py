# Maximum Earnings From Taxi
# Problem: https://leetcode.com/problems/maximum-earnings-from-taxi/

from typing import List
import bisect

class Solution:
    def maxTaxiEarnings(self, n: int, rides: List[List[int]]) -> int:
        # Sort by end time
        rides.sort(key=lambda x: x[1])
        
        # dp[i] = max earnings using subset of first i rides
        # dp stores pairs (end_time, max_earn)
        dp = [(0, 0)]
        
        for start, end, tip in rides:
            earn = end - start + tip
            
            # Find closest previous ride that ended <= start
            # bisect_right on list of pairs compares first element (end_time)
            idx = bisect.bisect_right(dp, (start, float('inf'))) - 1
            prev_earn = dp[idx][1]
            
            curr_total = prev_earn + earn
            
            if curr_total > dp[-1][1]:
                dp.append((end, curr_total))
                
        return dp[-1][1]

if __name__ == "__main__":
    solution = Solution()
    print(solution.maxTaxiEarnings(5, [[2,5,4],[1,5,1]]))  # Output: 7
