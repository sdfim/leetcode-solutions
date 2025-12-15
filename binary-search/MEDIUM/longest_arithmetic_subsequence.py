# Longest Arithmetic Subsequence
# Problem: https://leetcode.com/problems/longest-arithmetic-subsequence/

from typing import List

class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        # dp[i][diff] = length of arithmetic seq ending at i with difference diff.
        # Constraints: nums[i] <= 500. Length <= 1000.
        # Diff can range from -500 to 500. Offset by 500 to make index positive.
        
        n = len(nums)
        dp = {} # Using dict of dicts or list of dicts.
        
        # Optimizing: List of dicts is cleaner in Python.
        # Or since range is small, fixed array.
        # 1000 * 1000 ~ 10^6 states. Feasible.
        
        if n <= 2: return n
        
        ans = 2
        dp = [{} for _ in range(n)]
        
        for i in range(n):
            for j in range(i):
                diff = nums[i] - nums[j]
                
                # If we extend a subsequence from j with diff, length is dp[j][diff] + 1
                # Default is 2 (just j and i)
                current_len = dp[j].get(diff, 1) + 1
                dp[i][diff] = current_len
                ans = max(ans, current_len)
                
        return ans

if __name__ == "__main__":
    solution = Solution()
    print(solution.longestArithSeqLength([3,6,9,12])) # 4
