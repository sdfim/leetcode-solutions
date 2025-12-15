# Maximum Profit in Job Scheduling
# Problem: https://leetcode.com/problems/maximum-profit-in-job-scheduling/

from typing import List
import bisect

class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        jobs = sorted(zip(startTime, endTime, profit), key=lambda x: x[1])
        # dp[i] = max profit using subset of first i jobs (sorted by end time)
        # Store as (end_time, max_profit)
        dp = [(0, 0)]
        
        for s, e, p in jobs:
            # Find non-overlapping job ending <= s
            idx = bisect.bisect_right(dp, (s, float('inf'))) - 1
            curr_profit = dp[idx][1] + p
            
            if curr_profit > dp[-1][1]:
                dp.append((e, curr_profit))
                
        return dp[-1][1]

if __name__ == "__main__":
    solution = Solution()
    print(solution.jobScheduling([1,2,3,3], [3,4,5,6], [50,10,40,70]))  # Output: 120
