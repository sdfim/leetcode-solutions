# Path With Maximum Minimum Value
# Problem: https://leetcode.com/problems/path-with-maximum-minimum-value/

from typing import List
import heapq

class Solution:
    def maximumMinimumPath(self, grid: List[List[int]]) -> int:
        # We want to maximize the minimum value along path.
        # Dijkstra / Modified Prim's.
        # Use Max-Heap.
        
        m, n = len(grid), len(grid[0])
        # Max heap storing (val, r, c). Python heaps are min heaps, so store (-val, r, c)
        pq = [(-grid[0][0], 0, 0)]
        
        visited = [[False] * n for _ in range(m)]
        visited[0][0] = True
        
        # Current result is min value encountered so far in the path is NOT stored in PQ priority directly,
        # but the logic is: we always expand the node with highest capacity.
        # The 'bottleneck' is tracked.
        
        ans = grid[0][0]
        
        while pq:
            val, r, c = heapq.heappop(pq)
            val = -val
            ans = min(ans, val)
            
            if r == m - 1 and c == n - 1:
                return ans
                
            for dr, dc in [(0,1), (0,-1), (1,0), (-1,0)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and not visited[nr][nc]:
                    visited[nr][nc] = True
                    heapq.heappush(pq, (-grid[nr][nc], nr, nc))
                    
        return 0

if __name__ == "__main__":
    solution = Solution()
    print(solution.maximumMinimumPath([[5,4,5],[1,2,6],[7,4,6]])) # 4
