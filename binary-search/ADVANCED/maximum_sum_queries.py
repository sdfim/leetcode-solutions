# Maximum Sum Queries
# Problem: https://leetcode.com/problems/maximum-sum-queries/

from typing import List
import bisect

class Solution:
    def maximumSumQueries(self, nums1: List[int], nums2: List[int], queries: List[List[int]]) -> List[int]:
        # Offline processing.
        # Format: (nums1[i], nums2[i], sum[i])
        pairs = sorted([(nums1[i], nums2[i], nums1[i] + nums2[i]) for i in range(len(nums1))], key=lambda x: x[0], reverse=True)
        
        # Sort queries by x descending
        # Store index to restore result order
        qs = sorted([(queries[i][0], queries[i][1], i) for i in range(len(queries))], key=lambda x: x[0], reverse=True)
        
        ans = [-1] * len(queries)
        
        # Coordinate compression for nums2
        # Collect all nums2 values and query y values
        unique_vals = set(p[1] for p in pairs)
        for q in queries:
            unique_vals.add(q[1])
            
        sorted_coords = sorted(list(unique_vals))
        rank_map = {val: i+1 for i, val in enumerate(sorted_coords)}
        m = len(sorted_coords)
        
        # BIT for Max Suffix Query?
        # Standard BIT supports Prefix Max query efficiently (1..i).
        # We need Max in range [rank(y), m].
        # We can map coordinates such that we query [1, new_rank]?
        # If we use `new_rank = m - rank + 1`, then range [rank(y), m] becomes [1, m - rank(y) + 1].
        # So we can use standard BIT on reversed ranks.
        
        bit_tree = [-1] * (m + 1)
        
        def update(i, val):
            while i <= m:
                bit_tree[i] = max(bit_tree[i], val)
                i += i & (-i)
                
        def query(i):
            res = -1
            while i > 0:
                res = max(res, bit_tree[i])
                i -= i & (-i)
            return res
            
        pair_idx = 0
        n_pairs = len(pairs)
        
        for x, y, q_idx in qs:
            # Add all pairs with nums1 >= x
            while pair_idx < n_pairs and pairs[pair_idx][0] >= x:
                val = pairs[pair_idx][1]
                s = pairs[pair_idx][2]
                
                # Update BIT with nums2 = val
                # Reversed rank
                rank = rank_map[val]
                rev_rank = m - rank + 1
                update(rev_rank, s)
                
                pair_idx += 1
                
            # Query max sum with nums2 >= y
            rank_y = rank_map[y]
            rev_rank_y = m - rank_y + 1
            # We want values with original rank >= rank_y
            # In reversed coords, this means rev_rank <= rev_rank_y
            # So query(rev_rank_y) gives max of all items with rank >= rank_y
            
            ans[q_idx] = query(rev_rank_y)
            
        return ans

if __name__ == "__main__":
    solution = Solution()
    print(solution.maximumSumQueries([4,3,1,2], [2,4,9,5], [[4,1], [1,3], [2,5]]))
    # Output: [6, 10, 7]
