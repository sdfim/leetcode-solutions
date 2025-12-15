# Find the Index of Permutation
# Problem: https://leetcode.com/problems/find-the-index-of-permutation/
# Usually "Permutations of array", find lexicographical rank.

from typing import List

class Solution:
    def getPermutationIndex(self, perm: List[int]) -> int:
        # perm is a permutation of 1..n or 0..n-1.
        # Assume 1..n for standard description, adapt if 0-based.
        # Usually ans is modulo 10^9 + 7.
        
        MOD = 10**9 + 7
        n = len(perm)
        
        # BIT to count removed/seen elements
        # We need to count how many smaller available numbers exist.
        bit = [0] * (n + 1)
        
        def update(idx, val):
            while idx <= n:
                bit[idx] += val
                idx += idx & (-idx)
                
        def query(idx):
            s = 0
            while idx > 0:
                s += bit[idx]
                idx -= idx & (-idx)
            return s
            
        # Initially all numbers 1..n are available.
        # So count of smaller numbers available than X is X-1.
        # But as we use numbers, we need to track.
        # Easier: add all to BIT?
        # Start with BIT empty. Add numbers AS WE SEE THEM, so we can count how many smaller numbers were already used?
        # No.
        # We want: for position i with value val, count how many UNUSED numbers are < val.
        # Total unused smaller = (val - 1) - (count of used numbers < val).
        
        ans = 0
        
        # Precompute factorials
        fact = [1] * (n + 1)
        for i in range(2, n + 1):
            fact[i] = (fact[i-1] * i) % MOD
            
        for i, val in enumerate(perm):
            # Rank of this digit is (nums smaller than val not yet used) * (n - 1 - i)!
            
            used_smaller = query(val)
            # Assuming perm values are 1-based. If 0-based, adjust `val` to `val+1`.
            # If perm contains 1..n:
            smaller_avail = (val - 1) - used_smaller
            
            term = (smaller_avail * fact[n - 1 - i]) % MOD
            ans = (ans + term) % MOD
            
            update(val, 1)
            
        return ans

if __name__ == "__main__":
    solution = Solution()
    print(solution.getPermutationIndex([1, 2])) # 0 (if 0 indexed) or 1? usually 0-based index or 1-based rank?
    # Usually 0-based index asked.
    print(solution.getPermutationIndex([2, 1])) # 1
