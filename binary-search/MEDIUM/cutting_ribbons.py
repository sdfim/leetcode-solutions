# Cutting Ribbons
# Problem: https://leetcode.com/problems/cutting-ribbons/

from typing import List

class Solution:
    def maxLength(self, ribbons: List[int], k: int) -> int:
        left, right = 1, max(ribbons)
        res = 0
        
        while left <= right:
            mid = (left + right) // 2
            if mid == 0:
                left = 1
                continue
            
            count = sum(r // mid for r in ribbons)
            if count >= k:
                res = mid
                left = mid + 1
            else:
                right = mid - 1
        return res

if __name__ == "__main__":
    solution = Solution()
    print(solution.maxLength([9,7,5], 3))  # Output: 5
