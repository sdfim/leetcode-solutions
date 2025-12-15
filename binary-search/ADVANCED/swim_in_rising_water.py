# Swim in Rising Water
# Problem: https://leetcode.com/problems/swim-in-rising-water/

from typing import List
import heapq

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        # Dijkstra approach
        pq = [(grid[0][0], 0, 0)] # time, r, c
        visited = set([(0, 0)])
        res = 0
        
        while pq:
            t, r, c = heapq.heappop(pq)
            res = max(res, t)
            
            if r == n - 1 and c == n - 1:
                return res
            
            for nr, nc in [(r+1,c), (r-1,c), (r,c+1), (r,c-1)]:
                if 0 <= nr < n and 0 <= nc < n and (nr, nc) not in visited:
                    visited.add((nr, nc))
                    heapq.heappush(pq, (grid[nr][nc], nr, nc))
        return -1

if __name__ == "__main__":
    solution = Solution()
    print(solution.swimInWater([[0,2],[1,3]]))  # Output: 3
