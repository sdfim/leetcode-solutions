# Peak Index in a Mountain Array
# Problem: https://leetcode.com/problems/peak-index-in-a-mountain-array/

from typing import List

class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        left, right = 0, len(arr) - 1
        
        while left < right:
            mid = (left + right) // 2
            if arr[mid] < arr[mid + 1]:
                left = mid + 1
            else:
                right = mid
                
        return left

if __name__ == "__main__":
    solution = Solution()
    print(solution.peakIndexInMountainArray([0,1,0]))  # Output: 1
    print(solution.peakIndexInMountainArray([0,2,1,0])) # Output: 1
