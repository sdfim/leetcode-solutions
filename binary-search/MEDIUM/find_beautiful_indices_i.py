# Find Beautiful Indices in the Given Array I
# Problem: https://leetcode.com/problems/find-beautiful-indices-in-the-given-array-i/

from typing import List
import bisect

class Solution:
    def beautifulIndices(self, s: str, a: str, b: str, k: int) -> List[int]:
        # Helper to find all occurrences
        def find_occurrences(text, pattern):
            indices = []
            if not pattern: return indices
            start = 0
            while True:
                idx = text.find(pattern, start)
                if idx == -1:
                    break
                indices.append(idx)
                start = idx + 1 # Overlapping allowed? Problem usually says "indices i such that...". s[i:i+len(a)] == a. Yes.
            return indices
            
        indices_a = find_occurrences(s, a)
        indices_b = find_occurrences(s, b)
        
        ans = []
        if not indices_b:
            return ans
            
        indices_b.sort() # Should be sorted already but safe to ensure.
        
        for i in indices_a:
            # Check if there is j in indices_b such that |i - j| <= k.
            # i - k <= j <= i + k.
            
            idx = bisect.bisect_left(indices_b, i - k)
            if idx < len(indices_b) and indices_b[idx] <= i + k:
                ans.append(i)
                
        return ans

if __name__ == "__main__":
    solution = Solution()
    print(solution.beautifulIndices("isawsquirrelnearmysquirrelhouseohmy", "my", "squirrel", 15)) # [16, 33]
