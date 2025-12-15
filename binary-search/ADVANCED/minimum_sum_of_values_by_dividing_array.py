# Minimum Sum of Values by Dividing Array
# Problem: https://leetcode.com/problems/minimum-sum-of-values-by-dividing-array/

from typing import List
import functools

class Solution:
    def minimumValueSum(self, nums: List[int], andValues: List[int]) -> int:
        n = len(nums)
        m = len(andValues)
        inf = float('inf')
        
        @functools.lru_cache(None)
        def solve(idx, p_idx, current_and):
            if idx == n:
                return 0 if p_idx == m else inf
            
            if p_idx == m:
                return inf
                
            # Update current AND
            current_and &= nums[idx]
            
            # Pruning: The problem is that current_and can only decrease bits.
            # If current_and < andValues[p_idx], we can never reach equality (since we can't set bits back to 1).
            if current_and < andValues[p_idx]:
                return inf
                
            res = inf
            
            # Option 1: Continue current subarray
            # If current_and > target, we MUST continue (or we fail this segment).
            # Even if current_and == target, we CAN continue to see if it stays target (it might drop lower though).
            
            # Actually, typical DP state is (idx, p_idx, current_and).
            # But continuous segments of 'idx' will have same 'current_and'.
            # We can jump? No, just standard transition.
            
            # If current_and equals target, we can Try to end subarray here
            if current_and == andValues[p_idx]:
                sub_res = solve(idx + 1, p_idx + 1, -1) # -1 indicates new subarray starts (mask all 1s)
                if sub_res != inf:
                    res = min(res, nums[idx] + sub_res) # Wait, cost is 'value of last element'?
                    # The problem usually says: "sum of values of the last elements of each subarray".
                    # Let's assume cost is nums[idx].
            
            # Continue current subarray
            sub_res_cont = solve(idx + 1, p_idx, current_and)
            res = min(res, sub_res_cont)
            
            return res

        # Wrapper to handle initial -1 logic
        # solve(0, 0, -1) where -1 usually means all bits set for AND operation (e.g. 2^30 - 1)
        mask = (1 << 30) - 1
        ans = solve(0, 0, mask)
        return ans if ans != inf else -1

if __name__ == "__main__":
    solution = Solution()
    print(solution.minimumValueSum([2,3,5,7,7], [5,7])) # Example
