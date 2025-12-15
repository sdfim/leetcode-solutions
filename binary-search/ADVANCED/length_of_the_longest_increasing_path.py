# Length of the Longest Increasing Path
# Problem: https://leetcode.com/problems/longest-increasing-path-in-a-matrix/
# Note: Filename maps to standard problem Longest Increasing Path in a Matrix

from typing import List

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix: return 0
        m, n = len(matrix), len(matrix[0])
        memo = {}
        
        def dfs(r, c):
            if (r, c) in memo:
                return memo[(r, c)]
            
            val = matrix[r][c]
            res = 1
            
            # Directions: Up, Down, Left, Right
            directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and matrix[nr][nc] > val:
                    res = max(res, 1 + dfs(nr, nc))
            
            memo[(r, c)] = res
            return res
            
        ans = 0
        for i in range(m):
            for j in range(n):
                ans = max(ans, dfs(i, j))
                
        return ans

if __name__ == "__main__":
    solution = Solution()
    print(solution.longestIncreasingPath([[9,9,4],[6,6,8],[2,1,1]])) # Output: 4
