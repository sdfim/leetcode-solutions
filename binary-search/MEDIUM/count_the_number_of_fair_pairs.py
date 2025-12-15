# Count the Number of Fair Pairs
# Problem: https://leetcode.com/problems/count-the-number-of-fair-pairs/

from typing import List
import bisect

class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()
        n = len(nums)
        count = 0
        
        for i in range(n):
            # We want lower <= nums[i] + nums[j] <= upper, with i < j.
            # lower - nums[i] <= nums[j] <= upper - nums[i]
            
            min_val = lower - nums[i]
            max_val = upper - nums[i]
            
            # Find range in nums[i+1:]
            # But creating slices is slow. Use indices.
            
            left_idx = bisect.bisect_left(nums, min_val, lo=i+1)
            right_idx = bisect.bisect_right(nums, max_val, lo=i+1)
            
            count += (right_idx - left_idx)
            
        return count

if __name__ == "__main__":
    solution = Solution()
    print(solution.countFairPairs([0,1,7,4,4,5], 3, 6)) # 6
