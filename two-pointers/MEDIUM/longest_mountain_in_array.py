# Longest Mountain in Array
# Problem: https://leetcode.com/problems/longest-mountain-in-array/
# Solution:

from typing import List

class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        n = len(arr)
        if n < 3:
            return 0
            
        res = 0
        
        for i in range(1, n - 1):
            if arr[i-1] < arr[i] > arr[i+1]:
                l = i - 1
                r = i + 1
                
                while l > 0 and arr[l-1] < arr[l]:
                    l -= 1
                while r < n - 1 and arr[r] > arr[r+1]:
                    r += 1
                    
                res = max(res, r - l + 1)
                
        return res

if __name__ == "__main__":
    solution = Solution()
    
    arr1 = [2,1,4,7,3,2,5]
    print(f"Longest mountain in {arr1}: {solution.longestMountain(arr1)}")
