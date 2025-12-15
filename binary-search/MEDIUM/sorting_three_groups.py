# Sorting Three Groups
# Problem: https://leetcode.com/problems/sorting-three-groups/

from typing import List

class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        # Longest Non-Decreasing Subsequence with vals in {1,2,3}.
        # dp[val] = max length of non-decreasing subseq ending with value <= val.
        
        # Actually standard LIS.
        # Length of array - LIS length = min operations.
        # But LIS allows equal elements here? Yes, "Non-Decreasing".
        
        dp = [10**9] * len(nums) # Tails array for LIS? Not strictly tails since domain is small.
        # Simplify: dp[c] = Length of longest non-decreasing subsequence ending with value c.
        
        dp = [0] * 4 # Indices 1, 2, 3
        
        for x in nums:
            # If we pick x for current pos, valid prev are <= x.
            # Update order matters?
            # new_dp[x] = max(dp[1...x]) + 1
            # But since x is 1, 2, or 3, we can just update in place if careful.
            # Actually, standard O(N) since alphabet size is 3.
            
            # Since we want non-decreasing, if current is mapped to 1, prev must be 1.
            # If current is 2, prev 1 or 2.
            # If current is 3, prev 1, 2 or 3.
            # We want to change current x to target val.
            # Cost is 0 if x==target, 1 else.
            
            # Let dp[v] be min cost to solve prefix ending with value v.
            
            new_dp = [0] * 4
            cost1 = (1 if x != 1 else 0)
            cost2 = (1 if x != 2 else 0)
            cost3 = (1 if x != 3 else 0)
            
            new_dp[1] = dp[1] + cost1
            new_dp[2] = min(dp[1], dp[2]) + cost2
            new_dp[3] = min(dp[1], dp[2], dp[3]) + cost3
            
            dp = new_dp
            
        return min(dp[1], dp[2], dp[3])

if __name__ == "__main__":
    solution = Solution()
    print(solution.minimumOperations([2,1,3,2,1])) # 3
