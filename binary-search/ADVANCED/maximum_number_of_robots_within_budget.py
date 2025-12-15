# Maximum Number of Robots Within Budget
# Problem: https://leetcode.com/problems/maximum-number-of-robots-within-budget/

from typing import List
import collections

class Solution:
    def maximumRobots(self, chargeTimes: List[int], runningCosts: List[int], budget: int) -> int:
        n = len(chargeTimes)
        # We need max length k such that there exists a subarray of length k with cost <= budget.
        # Cost = max(chargeTimes) + k * sum(runningCosts).
        # We can binary search for k.
        # Or faster: Sliding Window.
        # As right increases, window grows. If cost > budget, shrink left.
        # We perform Max Sliding Window using Deque.
        
        dq = collections.deque() # stores indices
        current_run_sum = 0
        left = 0
        ans = 0
        
        for right in range(n):
            # Update sum
            current_run_sum += runningCosts[right]
            
            # Update Max Deque
            while dq and chargeTimes[dq[-1]] <= chargeTimes[right]:
                dq.pop()
            dq.append(right)
            
            # Check cost
            # current_k = right - left + 1
            # Run loop to shrink valid window
            # while valid...
            # Actually standard sliding window logic: "Find largest window ending at right?"
            # Or "Maintain valid window". If valid, update ans. If invalid, shrink.
            
            while left <= right:
                max_charge = chargeTimes[dq[0]]
                k = right - left + 1
                cost = max_charge + k * current_run_sum
                
                if cost > budget:
                    # Shrink
                    current_run_sum -= runningCosts[left]
                    if dq[0] == left:
                        dq.popleft()
                    left += 1
                else:
                    break
            
            ans = max(ans, right - left + 1)
            
        return ans

if __name__ == "__main__":
    solution = Solution()
    print(solution.maximumRobots([3,6,1,3,4], [2,1,3,4,5], 25)) # Output: 3
