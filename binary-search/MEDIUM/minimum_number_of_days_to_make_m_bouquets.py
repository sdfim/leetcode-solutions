# Minimum Number of Days to Make m Bouquets
# Problem: https://leetcode.com/problems/minimum-number-of-days-to-make-m-bouquets/

from typing import List

class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if m * k > len(bloomDay):
            return -1
            
        def can_make(days):
            bouquets = 0
            flowers = 0
            for d in bloomDay:
                if d <= days:
                    flowers += 1
                    if flowers == k:
                        bouquets += 1
                        flowers = 0
                else:
                    flowers = 0
            return bouquets >= m
            
        left, right = min(bloomDay), max(bloomDay)
        res = -1
        
        while left <= right:
            mid = (left + right) // 2
            if can_make(mid):
                res = mid
                right = mid - 1
            else:
                left = mid + 1
        return res

if __name__ == "__main__":
    solution = Solution()
    print(solution.minDays([1,10,3,10,2], 3, 1))  # Output: 3
