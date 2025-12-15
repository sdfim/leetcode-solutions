# Count Substrings That Satisfy K-Constraint II
# Problem: https://leetcode.com/problems/count-substrings-that-satisfy-k-constraint-ii/

from typing import List
import bisect

class Solution:
    def countKConstraintSubstrings(self, s: str, k: int, queries: List[List[int]]) -> List[int]:
        n = len(s)
        # Calculate 'left[i]': the smallest index such that s[left[i]...i] is valid.
        # Valid means count('0') <= k OR count('1') <= k.
        
        left_limit = [0] * n
        
        # Sliding window to find left boundary
        z_cnt = 0
        o_cnt = 0
        l = 0
        for r in range(n):
            if s[r] == '0': z_cnt += 1
            else: o_cnt += 1
            
            # While invalid, move left
            while z_cnt > k and o_cnt > k:
                if s[l] == '0': z_cnt -= 1
                else: o_cnt -= 1
                l += 1
            left_limit[r] = l
            
        # We need to answer sum_{i=L}^{R} (i - max(left_limit[i], L) + 1)
        # = sum_{i=L}^{R} (i + 1) - sum_{i=L}^{R} max(left_limit[i], L)
        
        # prefix sums for (i+1) is trivial or calculated formulaically.
        # Focus on sum max(left_limit[i], L).
        # left_limit is non-decreasing.
        # Find split point `idx` in [L, R] such that for i < idx, left_limit[i] < L (so max is L)
        # and for i >= idx, left_limit[i] >= L (so max is left_limit[i]).
        
        # Precompute prefix sums of left_limit
        prefix_left = [0] * (n + 1)
        for i in range(n):
            prefix_left[i+1] = prefix_left[i] + left_limit[i]
            
        results = []
        for L, R in queries:
            # Binary search for split point
            # Smallest idx >= L such that left_limit[idx] >= L
            idx = bisect.bisect_left(left_limit, L, lo=L, hi=R+1)
            
            # Range [L, idx-1]: items use L.
            count_L = idx - L
            sum_1 = count_L * L
            
            # Range [idx, R]: items use left_limit[i].
            sum_2 = prefix_left[R+1] - prefix_left[idx]
            
            total_subtract = sum_1 + sum_2
            
            # Total (i+1) sum
            # sum from l to r of (i+1) = (L+1 + R+1) * count / 2
            count_total = R - L + 1
            total_base = (L + 1 + R + 1) * count_total // 2
            
            ans = total_base - total_subtract
            results.append(ans)
            
        return results

if __name__ == "__main__":
    solution = Solution()
    print(solution.countKConstraintSubstrings("0001111", 2, [[0,6]])) # Example
