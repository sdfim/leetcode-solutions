# Most Beautiful Item for Each Query
# Problem: https://leetcode.com/problems/most-beautiful-item-for-each-query/

from typing import List
import bisect

class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        # Sort items by price
        items.sort()
        
        # Precompute max beauty up to index i
        # Filter items: keep only increasing beauty?
        # Or just store keys and query.
        
        prices = []
        max_beauty = []
        curr_max = 0
        
        for p, b in items:
            curr_max = max(curr_max, b)
            prices.append(p)
            max_beauty.append(curr_max)
            
        ans = []
        for q in queries:
            idx = bisect.bisect_right(prices, q) - 1
            if idx >= 0:
                ans.append(max_beauty[idx])
            else:
                ans.append(0)
                
        return ans

if __name__ == "__main__":
    solution = Solution()
    print(solution.maximumBeauty([[1,2],[3,2],[2,4],[5,6],[3,5]], [1,2,3,4,5,6])) 
    # [2, 4, 5, 5, 6, 6]
