# Find K Closest Elements
# Problem: https://leetcode.com/problems/find-k-closest-elements/

from typing import List

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # Binary search for the best starting position of the window of size k
        # We want to find index i such that arr[i...i+k-1] is best
        # Comparison: distance of arr[i] vs arr[i+k] to x
        # If x - arr[i] > arr[i+k] - x, then window should move right.
        
        left, right = 0, len(arr) - k
        
        while left < right:
            mid = (left + right) // 2
            
            if x - arr[mid] > arr[mid + k] - x:
                left = mid + 1
            else:
                right = mid
                
        return arr[left : left + k]

if __name__ == "__main__":
    solution = Solution()
    print(solution.findClosestElements([1,2,3,4,5], 4, 3))  # Output: [1,2,3,4]
