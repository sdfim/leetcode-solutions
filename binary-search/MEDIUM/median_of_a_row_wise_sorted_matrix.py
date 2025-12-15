# Median of a Row Wise Sorted Matrix
# Problem: https://leetcode.com/problems/median-of-a-row-wise-sorted-matrix/

from typing import List
import bisect

class Solution:
    def matrixMedian(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        total = m * n
        median_idx = total // 2
        
        # Range of values
        low = grid[0][0]
        high = grid[0][n-1]
        for i in range(1, m):
            low = min(low, grid[i][0])
            high = max(high, grid[i][n-1])
            
        ans = low
        
        while low <= high:
            mid = (low + high) // 2
            
            # Count elements <= mid
            count = 0
            for row in grid:
                count += bisect.bisect_right(row, mid)
                
            if count > median_idx:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
                
        return ans

if __name__ == "__main__":
    solution = Solution()
    print(solution.matrixMedian([[1,3,5],[2,6,9],[3,6,9]])) # 5
