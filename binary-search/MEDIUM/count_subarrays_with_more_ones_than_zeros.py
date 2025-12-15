# Count Subarrays With More Ones Than Zeros
# Problem: https://leetcode.com/problems/count-subarrays-with-more-ones-than-zeros/

from typing import List

class Solution:
    def subarrayWithMoreZerosThanOnes(self, nums: List[int]) -> int:
        # Wait, title is "With More Ones Than Zeros".
        # Treat 1 as 1, 0 as -1.
        # We want subarrays sum > 0.
        # Prefix sums. P[j] - P[i] > 0 => P[i] < P[j]. (i < j).
        # Count pairs (i, j) where i < j and P[i] < P[j].
        # This is effectively counting pairs (i, j) in an array such that i < j and val[i] < val[j].
        # But note P[0] = 0. We consider P[k] for k in 0...N.
        # This is basically "count inversions" but reversed (pairs in order).
        # Can use Fenwick Tree (BIT).
        
        MOD = 10**9 + 7
        
        # Transform nums
        vals = [1 if x == 1 else -1 for x in nums]
        prefix = [0] * (len(nums) + 1)
        for i in range(len(vals)):
            prefix[i+1] = prefix[i] + vals[i]
            
        # Helper for rank compression
        # We need to map prefix values to 1...M
        
        # Need to handle negative indices for BIT
        unique_vals = sorted(list(set(prefix)))
        rank_map = {v: i+1 for i, v in enumerate(unique_vals)}
        
        # BIT Implementation
        bit_size = len(unique_vals) + 1
        bit = [0] * bit_size
        
        def update(idx, val):
            while idx < bit_size:
                bit[idx] += val
                idx += idx & (-idx)
                
        def query(idx):
            s = 0
            while idx > 0:
                s += bit[idx]
                idx -= idx & (-idx)
            return s
            
        ans = 0
        # Iterate through prefix sums.
        # For current P[j], we want to count existing P[i] (where i < j) such that P[i] < P[j].
        # So we query count of numbers in BIT strictly less than P[j].
        # Then we add P[j] to BIT.
        
        for p in prefix:
            r = rank_map[p]
            # Count elements explicitly smaller
            count_smaller = query(r - 1)
            ans = (ans + count_smaller) % MOD
            update(r, 1)
            
        return ans

if __name__ == "__main__":
    solution = Solution()
    print(solution.subarrayWithMoreZerosThanOnes([0,1,1,0,1])) # 9
