# Maximum Enemy Forts That Can Be Captured
# Problem: https://leetcode.com/problems/maximum-enemy-forts-that-can-be-captured/
# Solution:

from typing import List

class Solution:
    def captureForts(self, forts: List[int]) -> int:
        res = 0
        l = 0
        
        for r in range(len(forts)):
            if forts[r] != 0:
                if forts[l] == -forts[r]:
                    res = max(res, r - l - 1)
                l = r
                
        return res

if __name__ == "__main__":
    solution = Solution()
    
    forts1 = [1,0,0,-1,0,0,0,0,1]
    print(f"Max captured forts in {forts1}: {solution.captureForts(forts1)}")
    
    forts2 = [0,0,1,-1]
    print(f"Max captured forts in {forts2}: {solution.captureForts(forts2)}")
