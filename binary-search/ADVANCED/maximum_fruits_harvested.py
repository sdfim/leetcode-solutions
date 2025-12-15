# Maximum Fruits Harvested After at Most K Steps
# Problem: https://leetcode.com/problems/maximum-fruits-harvested-after-at-most-k-steps/
# (LC 2106)

from typing import List
import bisect

class Solution:
    def maxTotalFruits(self, fruits: List[List[int]], startPos: int, k: int) -> int:
        # fruits: [[pos, amount]]. Sorted by pos.
        # We can move k steps from startPos.
        # Reachable interval [min_pos, max_pos].
        # dist(start, min) + dist(min, max) <= k  (Go left then right)
        # OR dist(start, max) + dist(max, min) <= k (Go right then left)
        # Equivalent: range [L, R] is valid if:
        # L <= start <= R: 
        #   cost = (start - L) + (R - L) <= k  => R - 2L + start <= k
        #   OR cost = (R - start) + (R - L) <= k => 2R - L - start <= k
        # Combined: R - L + min(|start - L|, |start - R|) <= k.
        
        # We iterate valid window [L, R].
        # Use simple Sliding Window or Two Pointers.
        # Since fruits are sparse positions, assume dense array? No, 2*10^5 positions.
        # Use the `fruits` array directly.
        # left index `l`, right index `r` in `fruits` array.
        
        n = len(fruits)
        
        # Prefix sums for fruit amounts
        # prefix[i] sum of amounts up to index i-1.
        # Amount in fruits[l...r] = prefix[r+1] - prefix[l].
        
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i+1] = prefix[i] + fruits[i][1]
            
        max_fruits = 0
        l = 0
        for r in range(n):
            # Check condition for window fruits[l...r]
            
            while l <= r:
                pos_l = fruits[l][0]
                pos_r = fruits[r][0]
                
                # Check if reachable from startPos
                # Condition: R - L + min(|start - L|, |start - R|) <= k
                # If start is outside [L, R], we definitely traverse path Start -> L -> R or Start -> R -> L.
                # Actually if start < L, we go Start -> R. Cost R - Start.
                # But here start can be inside.
                
                cost = 0
                if pos_r < startPos:
                    cost = startPos - pos_l
                elif pos_l > startPos:
                    cost = pos_r - startPos
                else:
                    d_left = startPos - pos_l
                    d_right = pos_r - startPos
                    cost = d_left + d_right + min(d_left, d_right)
                    
                if cost > k:
                    l += 1
                else:
                    break
            
            current = prefix[r+1] - prefix[l]
            max_fruits = max(max_fruits, current)
            
        return max_fruits

if __name__ == "__main__":
    solution = Solution()
    print(solution.maxTotalFruits([[2,8],[6,3],[8,6]], 5, 4)) # Output: 9
