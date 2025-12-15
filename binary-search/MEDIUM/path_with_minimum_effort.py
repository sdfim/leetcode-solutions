# Path With Minimum Effort
# Problem: https://leetcode.com/problems/path-with-minimum-effort/

from typing import List
import collections

class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        m, n = len(heights), len(heights[0])
        
        def can(k):
            # BFS to reach (m-1, n-1) with max diff <= k
            q = collections.deque([(0, 0)])
            visited = set([(0, 0)])
            while q:
                r, c = q.popleft()
                if r == m - 1 and c == n - 1:
                    return True
                
                for nr, nc in [(r+1,c), (r-1,c), (r,c+1), (r,c-1)]:
                    if 0 <= nr < m and 0 <= nc < n and (nr, nc) not in visited:
                        diff = abs(heights[nr][nc] - heights[r][c])
                        if diff <= k:
                            visited.add((nr, nc))
                            q.append((nr, nc))
            return False
            
        left, right = 0, 10**6
        res = right
        
        while left <= right:
            mid = (left + right) // 2
            if can(mid):
                res = mid
                right = mid - 1
            else:
                left = mid + 1
        return res

if __name__ == "__main__":
    solution = Solution()
    print(solution.minimumEffortPath([[1,2,2],[3,8,2],[5,3,5]]))  # Output: 2
