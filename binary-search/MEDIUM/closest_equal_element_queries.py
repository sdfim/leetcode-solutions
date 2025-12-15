# Closest Equal Element Queries
# Problem: https://leetcode.com/problems/closest-equal-element-queries/

from typing import List
import collections
import math

class Solution:
    def closestEqual(self, nums: List[int], queries: List[int]) -> List[int]:
        n = len(nums)
        # Store indices for each value
        pos = collections.defaultdict(list)
        for i, x in enumerate(nums):
            pos[x].append(i)
            
        # Precompute min distance for each index
        # To make it O(1) per query later
        min_dists = [-1] * n
        
        for val, indices in pos.items():
            k = len(indices)
            if k <= 1:
                # If only 1 occurrence, distance is -1 (no other equal element)
                for idx in indices:
                    min_dists[idx] = -1
                continue
                
            for i in range(k):
                current_idx = indices[i]
                
                # Neighbors in the sorted list of indices for this value
                prev_idx = indices[(i - 1 + k) % k]
                next_idx = indices[(i + 1) % k]
                
                # Distance to prev
                # In circular array, dist(a, b) = min(|a-b|, n - |a-b|)
                d1 = abs(current_idx - prev_idx)
                dist_prev = min(d1, n - d1)
                
                # Distance to next
                d2 = abs(current_idx - next_idx)
                dist_next = min(d2, n - d2)
                
                min_dists[current_idx] = min(dist_prev, dist_next)
                
        # Answer queries
        ans = []
        for q in queries:
            ans.append(min_dists[q])
            
        return ans

if __name__ == "__main__":
    solution = Solution()
    print(solution.closestEqual([1, 3, 1, 4, 1, 3, 2], [0, 3, 5])) # [2, -1, 3]
