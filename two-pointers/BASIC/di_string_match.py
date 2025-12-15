# DI String Match
# Problem: https://leetcode.com/problems/di-string-match/
# Solution:

from typing import List

class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        res = []
        low, high = 0, len(s)
        
        for c in s:
            if c == 'I':
                res.append(low)
                low += 1
            else:
                res.append(high)
                high -= 1
        res.append(low)
        return res

if __name__ == "__main__":
    solution = Solution()
    
    s1 = "IDID"
    print(f"DI String Match '{s1}': {solution.diStringMatch(s1)}")
    
    s2 = "III"
    print(f"DI String Match '{s2}': {solution.diStringMatch(s2)}")
