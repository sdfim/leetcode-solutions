# Count Negative Numbers in a Sorted Matrix
# Problem: https://leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix/

from typing import List

class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        count = 0
        for row in grid:
            # Binary Search finding first negative number
            left, right = 0, len(row) - 1
            first_neg_idx = len(row)
            
            while left <= right:
                mid = (left + right) // 2
                if row[mid] < 0:
                    first_neg_idx = mid
                    right = mid - 1
                else:
                    left = mid + 1
            
            count += len(row) - first_neg_idx
            
        return count

if __name__ == "__main__":
    solution = Solution()
    grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
    print(solution.countNegatives(grid))  # Output: 8
