# Minimized Maximum of Products Distributed to Any Store
# Problem: https://leetcode.com/problems/minimized-maximum-of-products-distributed-to-any-store/

from typing import List
import math

class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        def can(k):
            stores = 0
            for q in quantities:
                stores += math.ceil(q / k)
            return stores <= n
            
        left, right = 1, max(quantities)
        res = right
        
        while left <= right:
            mid = (left + right) // 2
            if mid == 0: # Avoid division by zero if left starts at 0 erroneously
                left = 1
                continue
            if can(mid):
                res = mid
                right = mid - 1
            else:
                left = mid + 1
        return res

if __name__ == "__main__":
    solution = Solution()
    print(solution.minimizedMaximum(6, [11,6]))  # Output: 3
