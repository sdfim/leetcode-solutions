# Maximum Total Damage With Spell Casting
# Problem: https://leetcode.com/problems/maximum-total-damage-with-spell-casting/

from typing import List
import collections
import bisect

class Solution:
    def maxTotalDamage(self, power: List[int]) -> int:
        freq = collections.Counter(power)
        unique_power = sorted(freq.keys())
        n = len(unique_power)
        
        # dp[i] = max damage using subset of first i+1 unique powers
        dp = [0] * n
        
        for i in range(n):
            curr_p = unique_power[i]
            damage = curr_p * freq[curr_p]
            
            # Previous state: exclude curr_p, just dp[i-1]
            prev_max = dp[i-1] if i > 0 else 0
            
            # Take curr_p. Must not take p-1, p-2 (or p+1, p+2).
            # We look for index j such that unique_power[j] < curr_p - 2.
            # i.e. unique_power[j] <= curr_p - 3. (Integers)
            
            # bisect_right returns insertion point.
            # items[:idx] are <= val.
            idx = bisect.bisect_right(unique_power, curr_p - 3)
            # Valid previous index is idx - 1 (if idx > 0)
            
            prev_valid = 0
            if idx > 0:
                prev_valid = dp[idx - 1]
                
            dp[i] = max(prev_max, prev_valid + damage)
            
        return dp[-1] if n > 0 else 0

if __name__ == "__main__":
    solution = Solution()
    print(solution.maxTotalDamage([1,1,3,4])) # 6
