# Escape the Spreading Fire
# Problem: https://leetcode.com/problems/escape-the-spreading-fire/

from typing import List
import collections

class Solution:
    def maximumMinutes(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        inf = 10**9
        
        # 1. BFS for Fire
        fire_time = [[inf] * n for _ in range(m)]
        fire_q = collections.deque()
        
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1:
                    fire_q.append((r, c))
                    fire_time[r][c] = 0
                elif grid[r][c] == 2:
                    fire_time[r][c] = -1 # Wall
        
        directions = [(0,1), (0,-1), (1,0), (-1,0)]
        
        while fire_q:
            r, c = fire_q.popleft()
            t = fire_time[r][c]
            
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] != 2 and fire_time[nr][nc] == inf:
                    fire_time[nr][nc] = t + 1
                    fire_q.append((nr, nc))
                    
        # 2. Check function
        def can_reach(wait_time):
            # Player starts at (0,0) at t = wait_time.
            # If fire reaches (0,0) at or before wait_time, fail.
            if fire_time[0][0] <= wait_time:
                return False
            
            visited = set()
            visited.add((0, 0))
            q = collections.deque([(0, 0, wait_time)])
            
            while q:
                r, c, t = q.popleft()
                
                # Try moves
                nt = t + 1
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] != 2 and (nr, nc) not in visited:
                        # Check fire condition
                        # If Safehouse: allowed if nt <= fire_time
                        # Else: allowed if nt < fire_time
                        
                        f_t = fire_time[nr][nc]
                        
                        valid = False
                        if nr == m - 1 and nc == n - 1:
                            if nt <= f_t:
                                valid = True
                                return True # Reached
                        else:
                            if nt < f_t:
                                valid = True
                                
                        if valid:
                            visited.add((nr, nc))
                            q.append((nr, nc, nt))
            return False

        # Binary Search
        # Upper bound: m * n or 10^9
        left, right = 0, m * n + 1000 # Heuristic max reasonable wait
        # If we can wait very long, return 10^9.
        # Check specific large value.
        
        if can_reach(10**9):
            return 10**9
            
        ans = -1
        while left <= right:
            mid = (left + right) // 2
            if can_reach(mid):
                ans = mid
                left = mid + 1
            else:
                right = mid - 1
                
        return ans

if __name__ == "__main__":
    solution = Solution()
    print(solution.maximumMinutes([[0,2,0,0,0,0,0],[0,0,0,2,2,1,0],[0,2,0,0,1,2,0],[0,0,2,2,2,0,2],[0,0,0,0,0,0,0]]))
    # Output: 3
