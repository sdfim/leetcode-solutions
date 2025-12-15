# Maximum Strictly Increasing Cells in a Matrix
# Problem: https://leetcode.com/problems/maximum-strictly-increasing-cells-in-a-matrix/

from typing import List
import collections

class Solution:
    def maxIncreasingCells(self, mat: List[List[int]]) -> int:
        if not mat: return 0
        m, n = len(mat), len(mat[0])
        
        # Group cells by value
        val_to_cells = collections.defaultdict(list)
        for r in range(m):
            for c in range(n):
                val_to_cells[mat[r][c]].append((r, c))
                
        sorted_vals = sorted(val_to_cells.keys())
        
        # Keep track of max path length ending in each row and col
        row_max = [0] * m
        col_max = [0] * n
        
        for v in sorted_vals:
            cells = val_to_cells[v]
            # Store updates to apply after processing all cells of value v.
            # This ensures we only transition from strictly smaller values.
            new_vals = []
            for r, c in cells:
                # Max path to here is 1 + max(best in row r so far, best in col c so far)
                new_vals.append(1 + max(row_max[r], col_max[c]))
                
            # Update the global row/col maxs
            for (r, c), val in zip(cells, new_vals):
                row_max[r] = max(row_max[r], val)
                col_max[c] = max(col_max[c], val)
                
        return max(max(row_max), max(col_max))

if __name__ == "__main__":
    solution = Solution()
    print(solution.maxIncreasingCells([[3,1],[3,4]])) # Output: 2
