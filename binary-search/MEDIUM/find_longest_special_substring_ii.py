# Find Longest Special Substring That Occurs Thrice I & II
# Problem: https://leetcode.com/problems/find-longest-special-substring-that-occurs-thrice-ii/

from typing import List
import collections

class Solution:
    def maximumLength(self, s: str) -> int:
        n = len(s)
        # Groups consecutive characters
        # e.g. "aaaa" -> ('a', 4)
        
        runs = collections.defaultdict(list)
        
        i = 0
        while i < n:
            start = i
            while i < n and s[i] == s[start]:
                i += 1
            length = i - start
            runs[s[start]].append(length)
            
        ans = -1
        
        # Check each character
        for char, lengths in runs.items():
            lengths.sort(reverse=True)
            if not lengths: continue
            
            # We want max L such that count is >= 3.
            # 1. Take top 3 lengths: l1, l2, l3 (pad with 0)
            l1 = lengths[0]
            l2 = lengths[1] if len(lengths) > 1 else 0
            l3 = lengths[2] if len(lengths) > 2 else 0
            
            # Case 1: Use 3 blocks from l1 alone.
            # If l1 is L, we can get L-2 with count 3. (L, L-1, L-2, L-? wait.)
            # e.g. "aaaaa" (5). substrings len 3: "aaa" (idx0), "aaa" (idx1), "aaa" (idx2). Count 3.
            # Formula: from length L run, we get `L - x + 1` substrings of length `x`.
            # We need `L - x + 1 >= 3` => `L - 2 >= x`.
            # Max x = L - 2.
            if l1 >= 3:
                ans = max(ans, l1 - 2)
            
            # Case 2: Use l1 and l2.
            # If l1 >= l2, we can assume we cut l1 to match l2?
            # From l1, we get plenty of l2 (at least 1, maybe more).
            # From l2, we get 1 of length l2.
            # Total count of length `x` where `x <= l2`.
            # Contribution from l1: `l1 - x + 1`.
            # Contribution from l2: `l2 - x + 1`.
            # We need sum >= 3. 
            # If we pick x = l2. l1 >= l2.
            # Count from l1 is at least 1.
            # Count from l2 is 1.
            # Total >= 2.
            # Could we get 3?
            # IF l1 > l2: then count from l1 is >= 2 (since l1 >= l2+1).
            # So if l1 > l2, then at len l2, we have >= 2 + 1 = 3.
            # So ans max l2.
            if l1 > l2:
                ans = max(ans, l2)
            else:
                # l1 == l2.
                # At len l2: count is 1 + 1 = 2. Not enough.
                # Try len l2 - 1.
                # l1 gives 2. l2 gives 2. Total 4.
                # So if l1 == l2, we can get l2 - 1.
                if l2 > 0:
                    ans = max(ans, l2 - 1)
            
            # Case 3: Use l1, l2, l3.
            # If l3 > 0, we have at least 1 of length l3 from each.
            # Total >= 3.
            ans = max(ans, l3)
            
        return ans

if __name__ == "__main__":
    solution = Solution()
    print(solution.maximumLength("aaaa")) # 2
    print(solution.maximumLength("abcdef")) # -1
    print(solution.maximumLength("abcaba")) # 1
