# Minimum Number of Flips to Make Binary Grid Palindromic I
# Problem: https://leetcode.com/problems/minimum-number-of-flips-to-make-binary-grid-palindromic-i/
# Solution:

from typing import List

class Solution:
    def minFlips(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        
        # Option 1: All rows palindromic
        row_flips = 0
        for i in range(m):
            l, r = 0, n - 1
            while l < r:
                if grid[i][l] != grid[i][r]:
                    row_flips += 1
                l += 1
                r -= 1
                
        # Option 2: All cols palindromic
        col_flips = 0
        for j in range(n):
            l, r = 0, m - 1
            while l < r:
                if grid[l][j] != grid[r][j]:
                    col_flips += 1
                l += 1
                r -= 1
                
        return min(row_flips, col_flips)

if __name__ == "__main__":
    solution = Solution()
    
    g1 = [[1,0,0],[0,0,0],[0,0,1]]
    print(f"Min flips I {g1}: {solution.minFlips(g1)}")
