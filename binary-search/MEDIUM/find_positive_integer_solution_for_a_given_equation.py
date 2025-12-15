# Find Positive Integer Solution for a Given Equation
# Problem: https://leetcode.com/problems/find-positive-integer-solution-for-a-given-equation/

from typing import List

# """
# This is the custom function interface.
# You should not implement it, or speculate about its implementation
# """
class CustomFunction:
    # Returns f(x, y) for any given positive integers x and y.
    # Note that f(x, y) is increasing with respect to both x and y.
    # i.e. f(x, y) < f(x + 1, y), f(x, y) < f(x, y + 1)
    def f(self, x, y):
        pass

class Solution:
    def findSolution(self, customfunction: 'CustomFunction', z: int) -> List[List[int]]:
        res = []
        # Two pointers approach (like searching in sorted matrix)
        x, y = 1, 1000
        
        while x <= 1000 and y >= 1:
            val = customfunction.f(x, y)
            if val == z:
                res.append([x, y])
                x += 1
                y -= 1 # Since increasing x increases value, need to decrease y
            elif val < z:
                x += 1
            else:
                y -= 1
        return res

if __name__ == "__main__":
    # Mock
    class MockFunc(CustomFunction):
        def f(self, x, y):
            return x + y
            
    solution = Solution()
    print(solution.findSolution(MockFunc(), 5))
