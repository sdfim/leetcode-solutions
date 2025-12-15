# Find Longest Special Substring That Occurs Thrice I
# Problem: https://leetcode.com/problems/find-longest-special-substring-that-occurs-thrice-i/

from typing import List
import collections

# Solution logic is identical to version II, just smaller constraints allow brute force too,
# but optimized logic works for both.

class Solution:
    def maximumLength(self, s: str) -> int:
        n = len(s)
        runs = collections.defaultdict(list)
        i = 0
        while i < n:
            start = i
            while i < n and s[i] == s[start]:
                i += 1
            runs[s[start]].append(i - start)
            
        ans = -1
        for char, lengths in runs.items():
            lengths.sort(reverse=True)
            if not lengths: continue
            
            l1 = lengths[0]
            l2 = lengths[1] if len(lengths) > 1 else 0
            l3 = lengths[2] if len(lengths) > 2 else 0
            
            # 1. From single run
            if l1 >= 3: ans = max(ans, l1 - 2)
            
            # 2. From two runs
            if l1 > l2:
                ans = max(ans, l2)
            elif l1 == l2:  # l1 == l2 implies we can perform l2 - 1
                if l2 > 0: ans = max(ans, l2 - 1)
            
            # 3. From three runs
            if l3 > 0:
                ans = max(ans, l3)
                
        return ans

if __name__ == "__main__":
    solution = Solution()
    print(solution.maximumLength("aaaa")) # 2
