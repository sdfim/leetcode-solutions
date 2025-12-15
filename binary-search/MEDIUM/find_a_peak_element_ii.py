# Find a Peak Element II
# Problem: https://leetcode.com/problems/find-a-peak-element-ii/

from typing import List

class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        m, n = len(mat), len(mat[0])
        # Binary search on columns or rows.
        # Pick mid row. Find max element in this row.
        # Compare with element above and below.
        # If max < below, peak is in lower half.
        # If max < above, peak is in upper half.
        # Else we found 2D peak.
        
        top, bottom = 0, m - 1
        while top <= bottom:
            mid_row = (top + bottom) // 2
            
            # Find max in mid_row
            max_col = 0
            for c in range(n):
                if mat[mid_row][c] > mat[mid_row][max_col]:
                    max_col = c
            
            val = mat[mid_row][max_col]
            upper = mat[mid_row - 1][max_col] if mid_row > 0 else -1
            lower = mat[mid_row + 1][max_col] if mid_row < m - 1 else -1
            
            if val > upper and val > lower:
                return [mid_row, max_col]
            elif val < upper:
                bottom = mid_row - 1
            else:
                top = mid_row + 1
                
        return []

if __name__ == "__main__":
    solution = Solution()
    print(solution.findPeakGrid([[1,4],[3,2]])) # [0,1] or [1,0]
