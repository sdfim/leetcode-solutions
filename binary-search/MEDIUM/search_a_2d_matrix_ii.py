# Search a 2D Matrix II
# Problem: https://leetcode.com/problems/search-a-2d-matrix-ii/

from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix: return False
        m, n = len(matrix), len(matrix[0])
        
        # Start from top-right corner
        row, col = 0, n - 1
        
        while row < m and col >= 0:
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] > target:
                col -= 1
            else:
                row += 1
                
        return False

if __name__ == "__main__":
    solution = Solution()
    print(solution.searchMatrix([[1,4,7],[2,5,8],[3,6,9]], 5)) # Output: True
