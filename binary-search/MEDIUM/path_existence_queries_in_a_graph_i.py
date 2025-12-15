# Path Existence Queries in a Graph I
# Problem: https://leetcode.com/problems/path-existence-queries-in-a-graph-i/

from typing import List

class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[bool]:
        # nums is sorted non-decreasing.
        # Nodes i and j connected if |nums[i] - nums[j]| <= maxDiff.
        # Since nums is sorted, connectivity is determined by adjacent differences.
        # If nums[i+1] - nums[i] <= maxDiff, then i and i+1 are connected.
        # Consequence: Connected components form contiguous segments [start, end].
        # We can precompute the component ID for each node.
        
        component = [0] * n
        comp_id = 0
        component[0] = 0
        
        for i in range(1, n):
            if nums[i] - nums[i-1] > maxDiff:
                comp_id += 1
            component[i] = comp_id
            
        ans = []
        for u, v in queries:
            ans.append(component[u] == component[v])
            
        return ans

if __name__ == "__main__":
    solution = Solution()
    print(solution.pathExistenceQueries(4, [1, 2, 4, 6], 2, [[0, 1], [0, 2], [2, 3]])) 
    # [1,2] diff 1 (<=2) -> linked. 
    # [2,4] diff 2 (<=2) -> linked.
    # [4,6] diff 2 (<=2) -> linked.
    # All linked? Yes. [True, True, True]
    print(solution.pathExistenceQueries(4, [1, 2, 5, 6], 2, [[0, 3]]))
    # 1-2 (ok), 2-5 (diff 3 > 2, break). 5-6 (ok).
    # Components: {0,1}, {2,3}. 0 and 3 not connected. [False]
