# Last Day Where You Can Still Cross
# Problem: https://leetcode.com/problems/last-day-where-you-can-still-cross/

from typing import List
import collections

class Solution:
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        # Binary search for day D.
        # Check if we can walk from top to bottom avoiding first D cells.
        
        def can_cross(day):
            grid = [[0] * col for _ in range(row)]
            for i in range(day):
                r, c = cells[i]
                grid[r-1][c-1] = 1 # 1 is blocked
                
            # BFS or DFS
            queue = collections.deque()
            visited = set()
            
            # Start from any open cell in top row
            for c in range(col):
                if grid[0][c] == 0:
                    queue.append((0, c))
                    visited.add((0, c))
            
            while queue:
                r, c = queue.popleft()
                if r == row - 1:
                    return True
                
                for dr, dc in [(0,1), (0,-1), (1,0), (-1,0)]:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < row and 0 <= nc < col and grid[nr][nc] == 0 and (nr, nc) not in visited:
                        visited.add((nr, nc))
                        queue.append((nr, nc))
            return False

        left, right = 0, len(cells)
        ans = 0
        
        while left <= right:
            mid = (left + right) // 2
            if can_cross(mid):
                ans = mid
                left = mid + 1
            else:
                right = mid - 1
        return ans

if __name__ == "__main__":
    solution = Solution()
    print(solution.latestDayToCross(2, 2, [[1,1],[2,1],[1,2],[2,2]])) # Output: 2
