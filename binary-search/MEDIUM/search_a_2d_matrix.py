# Search a 2D Matrix
# Problem: https://leetcode.com/problems/search-a-2d-matrix/

from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
            
        m, n = len(matrix), len(matrix[0])
        left, right = 0, m * n - 1
        
        while left <= right:
            mid = (left + right) // 2
            row = mid // n
            col = mid % n
            val = matrix[row][col]
            
            if val == target:
                return True
            elif val < target:
                left = mid + 1
            else:
                right = mid - 1
                
        return False

if __name__ == "__main__":
    solution = Solution()
    matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
    print(solution.searchMatrix(matrix, 3))  # Output: True
    print(solution.searchMatrix(matrix, 13)) # Output: False
