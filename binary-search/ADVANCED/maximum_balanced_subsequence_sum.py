# Maximum Balanced Subsequence Sum
# Problem: https://leetcode.com/problems/maximum-balanced-subsequence-sum/

from typing import List
import bisect

class Solution:
    def maxBalancedSubsequenceSum(self, nums: List[int]) -> int:
        # maximize sum of nums[i] s.t. indices i1 < i2 < ... < ik
        # and nums[ij] - nums[ij-1] >= ij - ij-1
        # => nums[ij] - ij >= nums[ij-1] - ij-1
        
        # Let values[i] = nums[i] - i
        # We need sum of subsequence such that values are non-decreasing.
        # This is equivalent to finding a subsequence with non-decreasing `values`, maximizing sum of `nums`.
        # DP: dp[i] = nums[i] + max(dp[j] for j < i where values[j] <= values[i], else 0)
        # Note: If max sum is negative, we can just take nums[i] itself?
        # Yes, standard recurrence: dp[i] = max(nums[i], nums[i] + query(values[i]))
        
        n = len(nums)
        vals = [nums[i] - i for i in range(n)]
        
        # Coordinate compression for BIT/SegmentTree
        sorted_vals = sorted(list(set(vals)))
        rank_map = {v: i + 1 for i, v in enumerate(sorted_vals)}
        m = len(sorted_vals)
        
        # MIT (Max Index Tree / Fenwick with Max)
        tree = [float('-inf')] * (m + 1)
        
        def update(idx, val):
            while idx <= m:
                tree[idx] = max(tree[idx], val)
                idx += idx & (-idx)
                
        def query(idx):
            res = float('-inf')
            while idx > 0:
                res = max(res, tree[idx])
                idx -= idx & (-idx)
            return res
            
        ans = float('-inf')
        
        for i in range(n):
            idx = rank_map[vals[i]]
            prev_max = query(idx)
            
            if prev_max == float('-inf'):
                current_sum = nums[i]
            else:
                # If prev_max is negative, adding it might not be optimal unless we are forced.
                # But subsequence sum can be negative?
                # Actually, if prev_max < 0, then max(nums[i], nums[i] + prev_max) = nums[i]
                current_sum = max(nums[i], nums[i] + prev_max)
                
            ans = max(ans, current_sum)
            update(idx, current_sum)
            
        return ans

if __name__ == "__main__":
    solution = Solution()
    print(solution.maxBalancedSubsequenceSum([3,3,5,6])) # Output: 14
