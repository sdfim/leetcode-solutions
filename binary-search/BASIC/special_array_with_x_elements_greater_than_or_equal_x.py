# Special Array With X Elements Greater Than or Equal X
# Problem: https://leetcode.com/problems/special-array-with-x-elements-greater-than-or-equal-x/

from typing import List
import bisect

class Solution:
    def specialArray(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        
        # Possible x values are from 0 to n
        for x in range(n + 1):
            idx = bisect.bisect_left(nums, x)
            count = n - idx
            if count == x:
                return x
                
        return -1

if __name__ == "__main__":
    solution = Solution()
    print(solution.specialArray([3,5]))  # Output: 2
    print(solution.specialArray([0,0]))  # Output: -1
