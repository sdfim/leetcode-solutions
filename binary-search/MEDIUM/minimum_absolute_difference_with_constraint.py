# Minimum Absolute Difference with Constraint
# Problem: https://leetcode.com/problems/minimum-absolute-difference-between-elements-with-constraint/

from typing import List
import bisect

class Solution:
    def minAbsoluteDifference(self, nums: List[int], x: int) -> int:
        if x == 0: return 0
        n = len(nums)
        infinite = float('inf')
        ans = infinite
        
        # Sorted list of nums[i] where i <= j - x
        sorted_window = []
        
        for j in range(x, n):
            # Add nums[j - x] to window
            val_to_add = nums[j - x]
            bisect.insort(sorted_window, val_to_add)
            
            target = nums[j]
            # Find closest in sorted_window
            idx = bisect.bisect_left(sorted_window, target)
            
            if idx < len(sorted_window):
                ans = min(ans, abs(sorted_window[idx] - target))
            if idx > 0:
                ans = min(ans, abs(sorted_window[idx-1] - target))
                
        return ans

if __name__ == "__main__":
    solution = Solution()
    print(solution.minAbsoluteDifference([4,3,2,4], 2)) # 0
