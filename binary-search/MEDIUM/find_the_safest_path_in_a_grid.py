# Find the Safest Path in a Grid
# Problem: https://leetcode.com/problems/find-the-safest-path-in-a-grid/

from typing import List
import collections

class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if grid[0][0] == 1 or grid[n-1][n-1] == 1:
            return 0
            
        # BFS to compute dist
        dist = [[-1] * n for _ in range(n)]
        q = collections.deque()
        
        for r in range(n):
            for c in range(n):
                if grid[r][c] == 1:
                    dist[r][c] = 0
                    q.append((r, c))
                    
        dirs = [(0,1), (0,-1), (1,0), (-1,0)]
        while q:
            r, c = q.popleft()
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n and dist[nr][nc] == -1:
                    dist[nr][nc] = dist[r][c] + 1
                    q.append((nr, nc))
                    
        # Binary search for safeness factor
        # Possible range 0 to 2*n
        low, high = 0, 2 * n
        ans = 0
        
        def check(limit):
            if dist[0][0] < limit: return False
            dq = collections.deque([(0, 0)])
            seen = set([(0, 0)])
            while dq:
                r, c = dq.popleft()
                if r == n-1 and c == n-1:
                    return True
                for dr, dc in dirs:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < n and 0 <= nc < n and (nr, nc) not in seen:
                        if dist[nr][nc] >= limit:
                            seen.add((nr, nc))
                            dq.append((nr, nc))
            return False
            
        while low <= high:
            mid = (low + high) // 2
            if check(mid):
                ans = mid
                low = mid + 1
            else:
                high = mid - 1
                
        return ans

if __name__ == "__main__":
    solution = Solution()
    print(solution.maximumSafenessFactor([[1,0,0],[0,0,0],[0,0,1]])) # 0
    print(solution.maximumSafenessFactor([[0,0,1],[0,0,0],[0,0,0]])) # 2
