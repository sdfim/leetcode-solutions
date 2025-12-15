# Fixed Point
# Problem: https://leetcode.com/problems/fixed-point/

from typing import List

class Solution:
    def fixedPoint(self, arr: List[int]) -> int:
        left, right = 0, len(arr) - 1
        res = -1
        
        while left <= right:
            mid = (left + right) // 2
            if arr[mid] == mid:
                res = mid
                right = mid - 1 # Find smallest index
            elif arr[mid] < mid:
                left = mid + 1
            else:
                right = mid - 1
                
        return res

if __name__ == "__main__":
    solution = Solution()
    print(solution.fixedPoint([-10,-5,0,3,7]))  # Output: 3
    print(solution.fixedPoint([0,2,5,8,17]))    # Output: 0
