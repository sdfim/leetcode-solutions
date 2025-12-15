# Most Profit Assigning Work
# Problem: https://leetcode.com/problems/most-profit-assigning-work/

from typing import List
import bisect

class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        jobs = sorted(zip(difficulty, profit))
        worker.sort()
        
        ans = 0
        max_p = 0
        i = 0
        n = len(jobs)
        
        # Two pointers approach (since both sorted)
        # Alternatively Binary Search for each worker
        
        for ability in worker:
            while i < n and jobs[i][0] <= ability:
                max_p = max(max_p, jobs[i][1])
                i += 1
            ans += max_p
            
        return ans

if __name__ == "__main__":
    solution = Solution()
    print(solution.maxProfitAssignment([2,4,6,8,10], [10,20,30,40,50], [4,5,6,7]))  # Output: 100
