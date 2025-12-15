# Find Beautiful Indices in the Given Array I
# Problem: https://leetcode.com/problems/find-beautiful-indices-in-the-given-array-i/
# Solution:

from typing import List

class Solution:
    def beautifulIndices(self, s: str, a: str, b: str, k: int) -> List[int]:
        def get_indices(main_s, sub_s):
            indices = []
            start = 0
            while True:
                idx = main_s.find(sub_s, start)
                if idx == -1:
                    break
                indices.append(idx)
                start = idx + 1
            return indices
            
        indices_a = get_indices(s, a)
        indices_b = get_indices(s, b)
        
        res = []
        j = 0
        
        for i in indices_a:
            while j < len(indices_b) and indices_b[j] < i - k:
                j += 1
            if j < len(indices_b) and abs(indices_b[j] - i) <= k:
                res.append(i)
                
        return res

if __name__ == "__main__":
    solution = Solution()
    
    s = "isawsquirrelnearmysquirrelhouseohmy"
    a = "my"
    b = "squirrel"
    k = 15
    print(f"Beautiful indices: {solution.beautifulIndices(s, a, b, k)}")
