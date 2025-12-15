# Sum of Square Numbers
# Problem: https://leetcode.com/problems/sum-of-square-numbers/
# Solution:

import math

class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        l = 0
        r = int(math.sqrt(c))
        
        while l <= r:
            cur = l*l + r*r
            if cur == c:
                return True
            elif cur > c:
                r -= 1
            else:
                l += 1
        return False

if __name__ == "__main__":
    solution = Solution()
    
    c1 = 5
    print(f"Sum of squares possible for {c1}: {solution.judgeSquareSum(c1)}")
    
    c2 = 3
    print(f"Sum of squares possible for {c2}: {solution.judgeSquareSum(c2)}")
