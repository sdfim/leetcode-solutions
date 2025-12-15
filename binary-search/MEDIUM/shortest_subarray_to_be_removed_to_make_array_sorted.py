# Shortest Subarray to be Removed to Make Array Sorted
# Problem: https://leetcode.com/problems/shortest-subarray-to-be-removed-to-make-array-sorted/

from typing import List

class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        n = len(arr)
        
        # Find longest non-decreasing prefix
        left = 0
        while left < n - 1 and arr[left] <= arr[left+1]:
            left += 1
            
        if left == n - 1:
            return 0
            
        # Find longest non-decreasing suffix
        right = n - 1
        while right > 0 and arr[right-1] <= arr[right]:
            right -= 1
            
        # Potential answers:
        # 1. Remove everything after prefix: result n - 1 - left
        # 2. Remove everything before suffix: result right
        # 3. Merge prefix and suffix
        
        ans = min(n - 1 - left, right)
        
        # Merge
        i = 0
        j = right
        while i <= left and j < n:
            if arr[i] <= arr[j]:
                # Valid merge: remove (i+1...j-1) -> len j - i - 1
                ans = min(ans, j - i - 1)
                i += 1
            else:
                j += 1
                
        return ans

if __name__ == "__main__":
    solution = Solution()
    print(solution.findLengthOfShortestSubarray([1,2,3,10,4,2,3,5]))  # Output: 3
