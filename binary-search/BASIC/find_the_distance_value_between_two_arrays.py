# Find the Distance Value Between Two Arrays
# Problem: https://leetcode.com/problems/find-the-distance-value-between-two-arrays/

from typing import List
import bisect

class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        arr2.sort()
        count = 0
        
        for val in arr1:
            # Find insertion point
            idx = bisect.bisect_left(arr2, val)
            
            valid = True
            # Check left neighbor
            if idx > 0 and abs(val - arr2[idx - 1]) <= d:
                valid = False
            # Check current/right neighbor elements
            if valid and idx < len(arr2) and abs(val - arr2[idx]) <= d:
                valid = False
            
            if valid:
                count += 1
                
        return count

if __name__ == "__main__":
    solution = Solution()
    print(solution.findTheDistanceValue([4,5,8], [10,9,1,8], 2))  # Output: 2
