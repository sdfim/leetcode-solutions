# Kth Smallest Amount With Single Denomination Combination
# Problem: https://leetcode.com/problems/kth-smallest-amount-with-single-denomination-combination/
# (LC 3116)

from typing import List
import math

class Solution:
    def findKthSmallest(self, coins: List[int], k: int) -> int:
        # Inclusion-Exclusion Principle.
        # sort coins, remove duplicates?
        coins = sorted(list(set(coins)))
        
        # Remove multiples (e.g. if 2 and 4 exist, 4 adds no new numbers).
        # Optimization: remove x if x % y == 0 for some y < x.
        unique_coins = []
        for x in coins:
            keep = True
            for y in unique_coins:
                if x % y == 0:
                    keep = False
                    break
            if keep:
                unique_coins.append(x)
        coins = unique_coins
        n = len(coins)
        
        # Precompute subset LCMs for Inclusion-Exclusion
        # Iterating 2^n might be slow if n=15 (32000 checks per binary search step).
        # We perform BS. 
        # Check(X) takes 2^n.
        # k up to 2*10^9. BS takes 60 steps.
        # 60 * 32000 ~ 2*10^6. Acceptable.
        
        subsets = [] # (lcm_val, sign)
        for i in range(1, 1 << n):
            lcm_val = 1
            cnt = 0
            for j in range(n):
                if (i >> j) & 1:
                    lcm_val = math.lcm(lcm_val, coins[j])
                    cnt += 1
                    # Optimization: if lcm huge, break?
                    if lcm_val > 10**15: # heuristic
                        break
            
            if lcm_val > 10**15:
                continue
                
            sign = 1 if cnt % 2 == 1 else -1
            subsets.append((lcm_val, sign))
            
        def count(x):
            ans = 0
            for val, sign in subsets:
                ans += sign * (x // val)
            return ans
            
        left, right = 1, min(coins) * k
        res = 0
        
        while left <= right:
            mid = (left + right) // 2
            if count(mid) >= k:
                res = mid
                right = mid - 1
            else:
                left = mid + 1
        return res

if __name__ == "__main__":
    solution = Solution()
    print(solution.findKthSmallest([3,6,9], 3)) # Output: 9
