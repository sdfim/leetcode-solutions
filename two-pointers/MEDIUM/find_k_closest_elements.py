# Find K Closest Elements
# Problem: https://leetcode.com/problems/find-k-closest-elements/
# Solution:

from typing import List

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        l, r = 0, len(arr) - 1
        
        while r - l + 1 > k:
            if abs(arr[l] - x) > abs(arr[r] - x):
                l += 1
            else:
                r -= 1
                
        return arr[l:r+1]

if __name__ == "__main__":
    solution = Solution()
    
    arr1 = [1,2,3,4,5]
    k1 = 4
    x1 = 3
    print(f"K closest elements in {arr1}, k={k1}, x={x1}: {solution.findClosestElements(arr1, k1, x1)}")
