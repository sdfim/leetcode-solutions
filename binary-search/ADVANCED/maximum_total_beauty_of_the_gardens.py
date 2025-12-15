# Maximum Total Beauty of the Gardens
# Problem: https://leetcode.com/problems/maximum-total-beauty-of-the-gardens/
# (LC 2234)

from typing import List
import bisect

class Solution:
    def maximumBeauty(self, flowers: List[int], newFlowers: int, target: int, full: int, partial: int) -> int:
        flowers.sort()
        n = len(flowers)
        
        # Count already full gardens
        # Optimization: Filter out flowers >= target? No, we can upgrade them effectively (cost 0).
        # But for beauty calculation, they are fixed as 'full'.
        # Actually we iterate how many gardens we FORCE to be full.
        # Gardens already >= target should be treated.
        
        # Suffix sum to help calculation
        # Or better: treat gardens < target.
        # If garden[i] >= target, strictly it is full. We can't reduce it.
        # So we split array into [ < target ] and [ >= target ].
        
        base_full_count = 0
        less = []
        for x in flowers:
            if x >= target:
                base_full_count += 1
            else:
                less.append(x)
        
        flowers = less
        n = len(flowers)
        
        # Prefix sums for cost calculation
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i+1] = prefix[i] + flowers[i]
            
        ans = 0
        
        # Iterate `i`: number of gardens we upgrade to FULL from the right end (largest values).
        # i ranges from 0 to n.
        # If valid, remaining newFlowers can improve minimum of remaining 0..n-i-1 gardens.
        
        for i in range(n + 1):
            # We make n-i gardens full (suffix).
            # Indices [0 ... n-i-1] are "partial" candidates.
            # Indices [n-i ... n-1] are upgraded to target.
            
            # Cost to upgrade suffix:
            # Need `target` for each. Current sum: prefix[n] - prefix[n-i].
            # Cost = `i * target - (sum of these i gardens)`.
            
            suffix_idx = n - i
            current_suffix_sum = prefix[n] - prefix[suffix_idx]
            cost_full = i * target - current_suffix_sum
            
            if cost_full > newFlowers:
                break # Cannot afford this many full gardens
                
            rem_flowers = newFlowers - cost_full
            
            # Maximize minimum of remaining gardens [0 ... suffix_idx - 1]
            if suffix_idx == 0:
                # All full
                score = (base_full_count + n) * full
                # partial term is 0? "if there are no incomplete gardens, beauty is full * count".
                ans = max(ans, score)
                continue
                
            # Binary search for max minimum `min_val`
            # We want largest `min_val` in range [flowers[0], target - 1].
            # Cost to make `prefix` gardens >= min_val:
            # Find closest index k such that flowers[k] >= min_val.
            # Upgrade flowers[0...k-1] to min_val.
            
            # Optimization:
            # Instead of inner BS, we can use BS over `min_val` range, or `idx`.
            # Max possible min_val is `target - 1`.
            # We can binary search on index `idx` such that we flatten up to `idx` to some level?
            # Actually easier to BS `min_v`.
            
            # Max min_v can be is bounded by average?
            # Or BS on min_val directly within [flowers[0], target-1].
            
            # Inner BS:
            l_v, r_v = flowers[0], target - 1
            best_min = flowers[0]
            
            # Optimized Inner BS:
            # Cost function is monotonic.
            while l_v <= r_v:
                mid = (l_v + r_v) // 2
                
                # Calculate cost to raise elements < mid to mid.
                # Find elements < mid.
                idx = bisect.bisect_left(flowers, mid, hi=suffix_idx)
                # Elements 0..idx-1 need upgrade.
                needed = idx * mid - prefix[idx]
                
                if needed <= rem_flowers:
                    best_min = mid
                    l_v = mid + 1
                else:
                    r_v = mid - 1
            
            score = (base_full_count + i) * full + best_min * partial
            ans = max(ans, score)
            
        return ans

if __name__ == "__main__":
    solution = Solution()
    print(solution.maximumBeauty([1,3,1,1], 7, 6, 12, 1)) # Output: 14
