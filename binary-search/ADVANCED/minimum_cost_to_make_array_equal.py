# Minimum Cost to Make Array Equal
# Problem: https://leetcode.com/problems/minimum-cost-to-make-array-equal/

from typing import List

class Solution:
    def minCost(self, nums: List[int], cost: List[int]) -> int:
        # The cost function f(x) = sum(abs(nums[i] - x) * cost[i])
        # This function is convex.
        # We can find the minimum using binary search on the derivative (or ternary search).
        # Alternatively, this is the weighted median problem.
        
        pairs = sorted(zip(nums, cost))
        total_cost = sum(cost)
        median_weight = (total_cost + 1) // 2
        
        current_weight = 0
        target = 0
        for num, c in pairs:
            current_weight += c
            if current_weight >= median_weight:
                target = num
                break
                
        # Calculate cost for target
        ans = 0
        for num, c in zip(nums, cost):
            ans += abs(num - target) * c
            
        return ans

if __name__ == "__main__":
    solution = Solution()
    print(solution.minCost([1,3,5,2], [2,3,1,14])) # Output: 8
