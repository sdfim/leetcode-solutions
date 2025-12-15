# Subsequence With the Minimum Score
# Problem: https://leetcode.com/problems/subsequence-with-the-minimum-score/
# (LC 2565)

class Solution:
    def minimumScore(self, s: str, t: str) -> int:
        n, m = len(s), len(t)
        
        # We want to remove substring t[i:j] such that remaining is subsequence of s.
        # Minimize length j - i.
        # 1. Compute prefix[k]: length of shortest prefix of s that contains t[0...k].
        # 2. Compute suffix[k]: length of shortest suffix of s that contains t[k...m-1].
        # Or better: `pre[i]` = index in `s` matching `t[0...i]` (min index).
        # `suf[i]` = index in `s` matching `t[i...m-1]` (max index).
        
        # Precompute pre array
        # pre[i] stores the index in s of the last character of t[0...i].
        # If not possible, inf.
        
        pre = [-1] * m
        s_idx = 0
        for i in range(m):
            while s_idx < n and s[s_idx] != t[i]:
                s_idx += 1
            if s_idx < n:
                pre[i] = s_idx
                s_idx += 1
            else:
                break # Remaining unmatched
                
        # Suffix array
        # suf[i] stores the index in s of the first character of t[i...m-1] matching from right.
        suf = [n] * m
        s_idx = n - 1
        for i in range(m - 1, -1, -1):
            while s_idx >= 0 and s[s_idx] != t[i]:
                s_idx -= 1
            if s_idx >= 0:
                suf[i] = s_idx
                s_idx -= 1
            else:
                break
                
        # Check removing substring t[l...r].
        # Remaining t[0...l-1] matches s using pre[l-1].
        # Remaining t[r+1...m-1] matches s using suf[r+1].
        # Valid if pre[l-1] < suf[r+1].
        
        # We want minimum score (length of removed).
        # Binary search for score? OR Two Pointers.
        # Iterate `l` (end of prefix kept). Maximize `start of suffix` that fits?
        # Actually easier: iterate `l` from -1 to `i` (where prefix exists).
        # Find smallest `r >= l` such that remaining [r+1...] fits.
        
        # Minimal removed length `d`. Check if valid.
        # Remove length `d`. Can we remove range of size `d`? 
        # Check `pre[i] < suf[i + d + 1]` for valid i.
        # Boundary cases: remove suffix t[m-d...m-1] (keep prefix m-d)?
        # Remove prefix t[0...d-1]?
        
        ans = m
        
        # Case 1: Keep prefix t[0...i] and suffix t[j...m-1].
        # i varies -1 to m-1.
        # j varies 0 to m.
        # Match t[0...i] using pre[i]. Need suf[j] > pre[i].
        # We want to minimize j - (i + 1) = remove length.
        
        # 1. Just suffix? (Keep empty prefix)
        # Find smallest j such that suf[j] >= -1 (always true, but need valid suf).
        # valid suf[j] < n means t[j...m-1] fits. Length removed = j.
        # Iterate j from 0. If suf[j] < n, ans = min(ans, j).
        
        # 2. Prefix + Suffix
        # Iterate i such that pre[i] matches (pre[i] < n).
        # We want smallest j > i such that suf[j] > pre[i].
        # We can enable binary search for j or two pointers.
        # Since pre[i] increases with i, required suf[j] increases, so valid j increases (shifts right).
        # Use two pointers.
        
        # Initial ans with full prefix check
        # i goes up to valid prefix end.
        k = -1
        while k + 1 < m and pre[k+1] != -1: # Wait, pre vals are indices. Initial check not needed if we iterate properly.
            pass
            
        # Proper iteration
        # Global minimum
        # Option: Remove everything -> m.
        
        # Option: Keep only prefix t[0...i]. Removed: m - 1 - i.
        # Valid if pre[i] < n.
        # Max valid i such that pre[i] != -1. 
        # Actually logic covers this if j=m.
        
        # Suffix-only logic
        import bisect
        # Finding best j for each i is O(M log M) or O(M).
        
        # Iterate i from -1 to m-1.
        # If i == -1: we keep nothing from prefix. Need valid suffix j.
        # suf[j] >= -1. Valid j is any j where suffix fits.
        # removed = j - 0 = j.
        
        j = 0
        while j < m and suf[j] == n:
            j += 1
        ans = min(ans, j)
        
        # Now consider i >= 0
        # Minimize j - i - 1 subject to suf[j] > pre[i]
        # Since i increases, pre[i] increases.
        # We need suf[j] > pre[i]. As constraint tightens, j must increase.
        # j is monotonic.
        
        j = 0
        for i in range(m):
            if pre[i] == -1: # prefix t[0...i] doesn't exist
                break
                
            # Keep t[0...i].
            # removed t[i+1...j-1]. Kept t[j...].
            # Need suf[j] > pre[i].
            # Move j forward until valid.
            while j < m and (j <= i or suf[j] <= pre[i]):
                j += 1
                
            # Removed t[i+1 ... j-1]. Length = j - 1 - (i+1) + 1 = j - i - 1.
            ans = min(ans, j - i - 1)
            
        return max(0, ans)

if __name__ == "__main__":
    solution = Solution()
    print(solution.minimumScore("abacaba", "bzaa")) # 1 (remove 'z')
