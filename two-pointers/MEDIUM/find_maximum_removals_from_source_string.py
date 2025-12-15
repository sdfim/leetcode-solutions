# Find Maximum Removals From Source String
# Problem: https://leetcode.com/problems/find-maximum-removals-from-source-string/
# Solution:

from typing import List

class Solution:
    def maxRemovals(self, source: str, pattern: str, targetIndices: List[int]) -> int:
        n = len(source)
        m = len(pattern)
        
        # dp[i][j] = max removals in source[:i] matching pattern[:j]
        # This is complex. Let's reframe.
        # We want to match pattern in source while maximizing removals from targetIndices.
        # This looks like DP.
        # dp[i][j] = min cost to match pattern[:j] using prefix source[:i].
        # Cost = number of skipped targetIndices.
        # We want to maximize removals => minimize kept target indices that are NOT used for pattern match?
        # No, we want to maximize removals of INDICES IN targetIndices.
        # So if we use an index in targetIndices for matching pattern, we cannot remove it.
        # If we don't use it, we can remove it (count + 1).
        
        target_set = set(targetIndices)
        dp = [-1] * (m + 1)
        dp[0] = 0 
        
        for i in range(n):
            # Iterate backwards to avoid using same source char for multiple pattern chars in one step
            for j in range(m - 1, -1, -1):
                if dp[j] != -1 and source[i] == pattern[j]:
                    # We can use source[i] to match pattern[j]
                    # If i is in target_set, we DON'T remove it. (gain 0)
                    # If i is NOT in target_set, we just use it. (gain 0)
                    # Wait, if we SKIP source[i] and it is in target_set, we gain 1.
                    
                    # Let dp[j] be max removals using prefix of source to match pattern[:j]
                    pass
            
            new_dp = list(dp)
            # If we skip source[i]:
            # If i in target, we increment all valid dp states by 1?
            # No, this is tricky because skipping means it's removed.
            
            # Let's switch state: dp[j] = max removals achievable after matching pattern[:j]
            # using some prefix of source ending at current i.
            
            is_target = i in target_set
            gain = 1 if is_target else 0
            
            # Update all reachable states from previous iteration by adding gain (since we skip this char)
            for k in range(m + 1):
                if dp[k] != -1:
                    new_dp[k] = max(new_dp[k], dp[k] + gain)
                    
            # Try to match source[i] with pattern[j]
            for j in range(m):
                if dp[j] != -1 and source[i] == pattern[j]:
                    # Consume source[i] for pattern[j]
                    # We cannot remove i. So gain is 0 from this i.
                    new_dp[j+1] = max(new_dp[j+1], dp[j]) # dp[j] already includes removals from previous chars
                    
            dp = new_dp
            
        return dp[m]

if __name__ == "__main__":
    solution = Solution()
    
    s1 = "abbaa"
    p1 = "aba"
    t1 = [0,1,2]
    print(f"Max removals: {solution.maxRemovals(s1, p1, t1)}")
