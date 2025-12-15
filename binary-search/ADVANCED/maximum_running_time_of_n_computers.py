# Maximum Running Time of N Computers
# Problem: https://leetcode.com/problems/maximum-running-time-of-n-computers/

from typing import List

class Solution:
    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        # Binary search on time T.
        # To run n computers for time T, we need total energy n * T.
        # Each battery can give at most T energy (since it can only power one computer at a time, 
        # but multiple computers consume energy in parallel, effectively we can swap efficiently).
        # Actually logic: total energy provided by batteries effectively capped at T per battery.
        # If sum(min(b, T) for b in batteries) >= n * T, then feasible.
        
        batteries.sort()
        
        left, right = 0, sum(batteries) // n
        res = 0
        
        while left <= right:
            mid = (left + right) // 2
            
            # Check feasibility
            # Optimize sum calculation
            # Use precomputed sum? Or just iterate? Iterate is O(M).
            # We can use binary search or prefix sums to speed up sum(min(b, mid)).
            
            # But plain iteration is acceptable given constraints usually?
            # Constraints: batteries length 10^5. n 10^5.
            # O(M * log MaxT).
            
            total_energy = 0
            for b in batteries:
                total_energy += min(b, mid)
                
            if total_energy >= n * mid:
                res = mid
                left = mid + 1
            else:
                right = mid - 1
        return res

if __name__ == "__main__":
    solution = Solution()
    print(solution.maxRunTime(2, [3,3,3])) # Output: 4
