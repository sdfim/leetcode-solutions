# Shortest Subarray to be Removed to Make Array Sorted
# Problem: https://leetcode.com/problems/shortest-subarray-to-be-removed-to-make-array-sorted/
# Solution:

from typing import List

class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        n = len(arr)
        left = 0
        while left < n - 1 and arr[left] <= arr[left+1]:
            left += 1
            
        if left == n - 1:
            return 0
            
        right = n - 1
        while right > 0 and arr[right] >= arr[right-1]:
            right -= 1
            
        result = min(n - left - 1, right)
        
        i, j = 0, right
        while i <= left and j < n:
            if arr[i] <= arr[j]:
                result = min(result, j - i - 1)
                i += 1
            else:
                j += 1
                
        return result

if __name__ == "__main__":
    solution = Solution()
    
    arr1 = [1,2,3,10,4,2,3,5]
    print(f"Shortest subarray removed from {arr1}: {solution.findLengthOfShortestSubarray(arr1)}")
    
    arr2 = [5,4,3,2,1]
    print(f"Shortest subarray removed from {arr2}: {solution.findLengthOfShortestSubarray(arr2)}")
