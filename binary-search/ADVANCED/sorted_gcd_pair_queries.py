# Sorted GCD Pair Queries
# Problem: https://leetcode.com/problems/sorted-gcd-pair-queries/
# (LC 3312)

from typing import List

class Solution:
    def gcdValues(self, nums: List[int], queries: List[int]) -> List[int]:
        # Count pairs (i, j) with gcd(nums[i], nums[j]) == g.
        # Use divisor counting logic.
        # max_val = max(nums). Count occurences of each number.
        
        max_val = max(nums)
        count = [0] * (max_val + 1)
        for x in nums:
            count[x] += 1
            
        # pairs_with_gcd_multiple_of[g]:
        # Count numbers divisible by g => C.
        # Pairs = C * (C - 1) / 2.
        
        count_g = [0] * (max_val + 1)
        
        # Sieve logic backwards
        for g in range(max_val, 0, -1):
            c = 0
            for multiple in range(g, max_val + 1, g):
                c += count[multiple]
            
            pairs = c * (c - 1) // 2
            
            # Subtract pairs with gcd 2g, 3g...
            for multiple in range(2 * g, max_val + 1, g):
                pairs -= count_g[multiple]
                
            count_g[g] = pairs
            
        # Transform to prefix sum over GCD values?
        # We need "Sorted GCD Pair Queries".
        # Pairs with GCD 1, then GCD 2... No, standard sort order is by value.
        # We have N pairs, GCDs are values.
        # We want to find the k-th smallest GCD?
        # If we list GCDs of all pairs sorted ascending.
        # We have `count_g[v]` pairs with GCD `v`.
        # Just prefix sum `count_g`.
        
        prefix = [0] * (max_val + 2)
        for g in range(1, max_val + 1):
            prefix[g+1] = prefix[g] + count_g[g]
            
        # Process queries
        # q is 0-indexed index in sorted array of GCDs.
        # Find smallest g such that prefix[g+1] > q.
        # Since count_g is for value 'g'.
        # GCD values 1..1.. (count_g[1] times), 2..2.. (count_g[2] times), etc.
        
        res = []
        import bisect
        for q in queries:
            # We want g.
            # bisect_right on prefix.
            idx = bisect.bisect_right(prefix, q)
            # idx is index in prefix. prefix[idx] <= q < prefix[idx+1]?
            # bisect_right returns insertion point.
            # prefix[i] <= q < prefix[i+1] means we are in bucket `i`.
            # prefix array is shifted by 1. prefix[1] = count[0], prefix[2] = count[0]+count[1]...
            # Actually prefix[g+1] accumulates sum(count_g[0...g]).
            # q within [prefix[g], prefix[g+1]) => answer is g.
            # bisect_right on prefix: finds first elements > q.
            # let `idx` be result.
            # prefix[idx] > q. prefix[idx-1] <= q.
            # So answer is `idx - 1`.
            res.append(idx - 1)
            
        return res

if __name__ == "__main__":
    solution = Solution()
    print(solution.gcdValues([2,3,4], [0,2])) # Example
