# Leftmost Column with at Least a One
# Problem: https://leetcode.com/problems/leftmost-column-with-at-least-a-one/

# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
class BinaryMatrix(object):
    def get(self, row: int, col: int) -> int:
        pass
    def dimensions(self) -> list[int]:
        pass

class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        m, n = binaryMatrix.dimensions()
        curr_row = 0
        curr_col = n - 1
        ans = -1
        
        # Start top-right
        # While within bounds:
        # If 0, move down (this row can't provide better answer than we are at)
        # If 1, record ans = col, move left to check for earlier 1s
        
        while curr_row < m and curr_col >= 0:
            if binaryMatrix.get(curr_row, curr_col) == 1:
                ans = curr_col
                curr_col -= 1
            else:
                curr_row += 1
                
        return ans

if __name__ == "__main__":
    # Mock
    class MockMatrix(BinaryMatrix):
        def __init__(self, mat):
            self.mat = mat
        def get(self, r, c):
            return self.mat[r][c]
        def dimensions(self):
            return [len(self.mat), len(self.mat[0])]
            
    mat = [[0,0],[1,1]]
    solution = Solution()
    print(solution.leftMostColumnWithOne(MockMatrix(mat)))  # Output: 0
