# Maximize the Profit as the Salesman
# Problem: https://leetcode.com/problems/maximize-the-profit-as-the-salesman/

from typing import List
import collections

class Solution:
    def maximizeTheProfit(self, n: int, offers: List[List[int]]) -> int:
        # dp[i] = max profit using houses 0..i-1 (length i prefix)
        # offers[j] = [start, end, gold]. 0-indexed.
        
        # Group offers by ENDing location.
        # offers_by_end[e] = list of (start, gold)
        
        offers_by_end = collections.defaultdict(list)
        for s, e, g in offers:
            offers_by_end[e].append((s, g))
            
        dp = [0] * (n + 1)
        
        for i in range(1, n + 1):
            # Option 1: Don't sell house i-1
            dp[i] = dp[i-1]
            
            # Option 2: Sell house i-1 via some offer ending at i-1
            for start, gold in offers_by_end[i-1]:
                # We use houses start to i-1.
                # Profit is dp[start] + gold.
                dp[i] = max(dp[i], dp[start] + gold)
                
        return dp[n]

if __name__ == "__main__":
    solution = Solution()
    print(solution.maximizeTheProfit(5, [[0,0,1],[0,2,2],[1,3,2]])) # 3
