# Assign Cookies
# Problem: https://leetcode.com/problems/assign-cookies/
# Solution:

from typing import List

class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        
        i, j = 0, 0
        count = 0
        
        while i < len(g) and j < len(s):
            if s[j] >= g[i]:
                count += 1
                i += 1
            j += 1
            
        return count

if __name__ == "__main__":
    solution = Solution()
    
    g1 = [1,2,3]
    s1 = [1,1]
    print(f"Content children g={g1}, s={s1}: {solution.findContentChildren(g1, s1)}")
