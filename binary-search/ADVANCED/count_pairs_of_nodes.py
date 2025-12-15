# Count Pairs of Nodes
# Problem: https://leetcode.com/problems/count-pairs-of-nodes/

from typing import List, Counter
import collections

class Solution:
    def countPairs(self, n: int, edges: List[List[int]], queries: List[int]) -> List[int]:
        # degrees
        deg = [0] * (n + 1)
        # Shared edges count
        shared = collections.defaultdict(int)
        
        for u, v in edges:
            if u > v: u, v = v, u
            deg[u] += 1
            deg[v] += 1
            shared[(u, v)] += 1
            
        sorted_deg = sorted(deg[1:])
        
        res = []
        for q in queries:
            count = 0
            # 1. Count pairs (i, j) such that deg[i] + deg[j] > q using two pointers on sorted_deg
            l, r = 0, n - 1
            while l < r:
                if sorted_deg[l] + sorted_deg[r] > q:
                    count += (r - l)
                    r -= 1
                else:
                    l += 1
            
            # 2. Adjust for shared edges.
            # If for a pair (u, v), deg[u] + deg[v] > q BUT deg[u] + deg[v] - shared > q is FALSE,
            # we counted it in step 1 incorrectly (we assumed it's valid).
            # Wait, step 1 counts pairs based on sum of degrees.
            # Actual condition: deg[u] + deg[v] - shared(u, v) > q.
            # So if deg[u] + deg[v] > q but deg[u] + deg[v] - shared <= q, we should decrement.
            
            for (u, v), sh in shared.items():
                if deg[u] + deg[v] > q:
                    if deg[u] + deg[v] - sh <= q:
                        count -= 1
                        
            res.append(count)
            
        return res

if __name__ == "__main__":
    solution = Solution()
    print(solution.countPairs(4, [[1,2],[2,4],[1,3],[2,3],[2,1]], [2, 3]))
    # Output: [6, 5]
