# Shortest Distance to Target Color
# Problem: https://leetcode.com/problems/shortest-distance-to-target-color/

from typing import List
import bisect
import collections

class Solution:
    def shortestDistanceColor(self, colors: List[int], queries: List[List[int]]) -> List[int]:
        color_indices = collections.defaultdict(list)
        for i, c in enumerate(colors):
            color_indices[c].append(i)
            
        res = []
        for i, c in queries:
            if c not in color_indices:
                res.append(-1)
                continue
            
            indices = color_indices[c]
            idx = bisect.bisect_left(indices, i)
            
            dist = float('inf')
            # Check left neighbor
            if idx > 0:
                dist = min(dist, i - indices[idx - 1])
            # Check current/right neighbor
            if idx < len(indices):
                dist = min(dist, indices[idx] - i)
                
            res.append(dist)
            
        return res

if __name__ == "__main__":
    solution = Solution()
    print(solution.shortestDistanceColor([1,1,2,1,3,2,2,3,3], [[1,3],[2,2],[6,1]]))  # Output: [3,0,3]
