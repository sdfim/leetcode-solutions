# Kth Missing Positive Number
# Problem: https://leetcode.com/problems/kth-missing-positive-number/

from typing import List

class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        left, right = 0, len(arr) - 1
        
        while left <= right:
            mid = (left + right) // 2
            # Number of missing integers before arr[mid] is arr[mid] - (mid + 1)
            missing = arr[mid] - (mid + 1)
            
            if missing < k:
                left = mid + 1
            else:
                right = mid - 1
                
        # The number of missing integers at index 'right' is arr[right] - (right + 1)
        # We need (k - missing) more integers
        # Result is arr[right] + (k - missing)
        # = arr[right] + k - (arr[right] - (right + 1))
        # = arr[right] + k - arr[right] + right + 1
        # = k + right + 1
        # Since left = right + 1 after loop
        # Result = k + left
        
        return k + left

if __name__ == "__main__":
    solution = Solution()
    print(solution.findKthPositive([2,3,4,7,11], 5))  # Output: 9
    print(solution.findKthPositive([1,2,3,4], 2))     # Output: 6
