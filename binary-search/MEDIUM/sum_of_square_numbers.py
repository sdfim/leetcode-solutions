# Sum of Square Numbers
# Problem: https://leetcode.com/problems/sum-of-square-numbers/

import math

class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        left, right = 0, int(math.isqrt(c))
        
        while left <= right:
            s = left*left + right*right
            if s == c:
                return True
            elif s < c:
                left += 1
            else:
                right -= 1
        return False

if __name__ == "__main__":
    solution = Solution()
    print(solution.judgeSquareSum(5))  # Output: True
