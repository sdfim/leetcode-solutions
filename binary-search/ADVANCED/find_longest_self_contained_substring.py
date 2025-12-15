# Find Longest Self-Contained Substring
# Problem: https://leetcode.com/problems/find-longest-self-contained-substring/

from typing import List

class Solution:
    def maxSubstringLength(self, s: str) -> int:
        n = len(s)
        # Self-contained: all chars in s[i..j] appear ONLY in s[i..j].
        # Length < n.
        
        # 1. Compute first and last occurrences of each char.
        first = {}
        last = {}
        for i, c in enumerate(s):
            if c not in first: first[c] = i
            last[c] = i
            
        # Iterate over all 26 chars as potential "start char" of the substring?
        # A valid substring must start at `first[c]` for some c?
        # No. Example "abba". "bb" is self-contained. starts at 1. first['b'] is 1.
        # Yes, if 'b' is in the substring, and substring is self-contained, 
        # then ALL 'b's must be in it. So range must include [first['b'], last['b']].
        
        # So a valid substring is a union of intervals [first[c], last[c]] for all c in it.
        # This implies that if any c is in it, the full interval I_c is in it.
        # So valid substrings are Unions of intervals of their components.
        # Let intervals be I_a, I_b, ...
        # If I_a overlaps I_b, they must merge.
        # If we pick a set of chars, their merged interval must exactly contain that set of chars.
        
        # We can try each character `c` as the "seed".
        # Assume `c` is in the substring.
        # Then we MUST include `[first[c], last[c]]`.
        # Expand this interval: for every char `x` inside, we MUST include `[first[x], last[x]]`.
        # Repeat until stable.
        # If stable interval length < n, record max.
        
        ans = -1
        unique_chars = sorted(first.keys())
        
        for c in unique_chars:
            # Expand from c
            current_start, current_end = first[c], last[c]
            
            # Optimization: If we already found a valid substring containing `c` that is larger than current candidate?
            # Or if `c` was processed as part of another seed?
            # Just do simple expansion. Max 26 iterations. Steps limit is N.
            # Total complexity 26 * N.
            
            valid = True
            k = current_start
            while k <= current_end:
                char_k = s[k]
                # Expand range
                current_start = min(current_start, first[char_k])
                current_end = max(current_end, last[char_k]) # May extend right
                
                # If current_start moves left, we might need to re-check indices < original k?
                # Actually, simply restart loop or maintain global min/max?
                # If current_start < k (original start), we need to check chars in [current_start, k].
                # Simplest is to keep checking until processed everything in [current_start, current_end].
                
                # Careful loop logic:
                # We need to scan all chars in [current_start, current_end].
                # If during scan we extend bounds, we continue scanning strictly.
                # Just iterate index `scan` from `current_start`.
                if current_start < first[c]: 
                     # Optimization: if we expanded left beyond seed's first, maybe this gets duplicated?
                     # No problem.
                     pass
                k += 1
                
            # Correct expansion implementation:
            cur_l, cur_r = first[c], last[c]
            
            # Scan pointer
            p = cur_l
            while p <= cur_r:
                char_p = s[p]
                
                # If any char starts before cur_l, expand left
                if first[char_p] < cur_l:
                    cur_l = first[char_p]
                    # Since we moved left, we must scan the new prefix
                    p = cur_l # Restart scan from new left?
                    # This could loop O(N^2) worst case?
                    # Actually bounds only grow. Max expansions is 26.
                    # Just setting p = cur_l is correct?
                    # Yes, re-evaluate from new boundary.
                
                # If any char ends after cur_r, expand right
                if last[char_p] > cur_r:
                    cur_r = last[char_p]
                
                p += 1
                
            # Check if valid (not whole string)
            if cur_r - cur_l + 1 < n:
                ans = max(ans, cur_r - cur_l + 1)
                
        return ans

if __name__ == "__main__":
    solution = Solution()
    print(solution.maxSubstringLength("abba")) # 2 ("bb")
