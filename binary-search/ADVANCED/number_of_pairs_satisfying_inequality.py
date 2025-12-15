# Number of Pairs Satisfying Inequality
# Problem: https://leetcode.com/problems/number-of-pairs-satisfying-inequality/
# (LC 2426)

from typing import List

class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], diff: int) -> int:
        # nums1[i] - nums1[j] <= nums2[i] - nums2[j] + diff
        # (nums1[i] - nums2[i]) <= (nums1[j] - nums2[j]) + diff
        # Let C[i] = nums1[i] - nums2[i].
        # Find pairs i < j such that C[i] <= C[j] + diff.
        # C[i] - diff <= C[j].
        
        # Iterate j from 0 to n-1.
        # Count i < j such that C[i] <= C[j] + diff.
        # Use BIT or Merge Sort.
        # Values can be negative, offset them.
        
        n = len(nums1)
        C = [x - y for x, y in zip(nums1, nums2)]
        
        # Coordinate compression
        vals = set(C)
        for x in C:
            vals.add(x + diff)
        
        sorted_vals = sorted(list(vals))
        rank_map = {val: i + 1 for i, val in enumerate(sorted_vals)}
        m = len(sorted_vals)
        
        tree = [0] * (m + 1)
        
        def update(i, delta):
            while i <= m:
                tree[i] += delta
                i += i & (-i)
                
        def query(i):
            s = 0
            while i > 0:
                s += tree[i]
                i -= i & (-i)
            return s
            
        ans = 0
        for x in C:
            # We want count of C[i] <= C[j] + diff
            # Current x is C[j].
            target = x + diff
            r = rank_map[target]
            count = query(r)
            ans += count
            
            # Add x to BIT
            update(rank_map[x], 1)
            
        return ans

if __name__ == "__main__":
    solution = Solution()
    print(solution.numberOfPairs([3,2,5], [2,2,1], 1)) # 3
