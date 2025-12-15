# Find Beautiful Indices in the Given Array II
# Problem: https://leetcode.com/problems/find-beautiful-indices-in-the-given-array-ii/

from typing import List
import bisect

class Solution:
    def beautifulIndices(self, s: str, a: str, b: str, k: int) -> List[int]:
        # Beautiful index i:
        # 1. s[i : i + len(a)] == a
        # 2. There exists index j such that s[j : j + len(b)] == b
        # 3. |j - i| <= k
        
        # 1. Find all occurrences of a.
        # 2. Find all occurrences of b.
        # Time complexity: O(N) using KMP or Z-algorithm. Python's find is fast but O(N*M) worst case?
        # Constraints: s length 5 * 10^5. a, b length small? No, can be up to N.
        # Python's `s.find` or `string in string` is Boyer-Moore-like, usually fast but technically O(NM).
        # We need strict KMP for competitive strictness, but standard built-in usually passes.
        # Let's use KMP for robustness in "Advanced". (Or just find all).
        
        def get_occurrences(text, pattern):
            # KMP
            if not pattern: return []
            n_t, n_p = len(text), len(pattern)
            lps = [0] * n_p
            
            # Compute LPS
            length = 0
            i = 1
            while i < n_p:
                if pattern[i] == pattern[length]:
                    length += 1
                    lps[i] = length
                    i += 1
                else:
                    if length != 0:
                        length = lps[length - 1]
                    else:
                        lps[i] = 0
                        i += 1
                        
            ans = []
            i = 0 # text index
            j = 0 # pattern index
            while i < n_t:
                if pattern[j] == text[i]:
                    i += 1
                    j += 1
                    
                if j == n_p:
                    ans.append(i - j)
                    j = lps[j-1]
                elif i < n_t and pattern[j] != text[i]:
                    if j != 0:
                        j = lps[j-1]
                    else:
                        i += 1
            return ans

        indices_a = get_occurrences(s, a)
        indices_b = get_occurrences(s, b) # Sorted by definition
        
        if not indices_b:
            return []
            
        res = []
        for i in indices_a:
            # Check if there is a j in indices_b with |j - i| <= k
            # range [i - k, i + k]
            # Use bisect to find closest j
            
            # Find insertion point for i
            pos = bisect.bisect_left(indices_b, i)
            
            # Check indices_b[pos] (>= i) and indices_b[pos-1] (< i)
            found = False
            if pos < len(indices_b):
                if abs(indices_b[pos] - i) <= k:
                    found = True
            
            if not found and pos > 0:
                if abs(indices_b[pos-1] - i) <= k:
                    found = True
                    
            if found:
                res.append(i)
                
        return res

if __name__ == "__main__":
    solution = Solution()
    print(solution.beautifulIndices("isawsquirrelnearmysquirrelhouseohmy", "my", "squirrel", 15))
    # Output: [16, 33]
