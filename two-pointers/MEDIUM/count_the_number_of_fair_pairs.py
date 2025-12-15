# Count the Number of Fair Pairs
# Problem: https://leetcode.com/problems/count-the-number-of-fair-pairs/
# Solution:

from typing import List
import bisect

class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()
        count = 0
        
        for i in range(len(nums)):
            # Find range [l, r] such that lower <= nums[i] + val <= upper
            low_idx = bisect.bisect_left(nums, lower - nums[i], i + 1)
            high_idx = bisect.bisect_right(nums, upper - nums[i], i + 1)
            count += high_idx - low_idx
            
        return count

if __name__ == "__main__":
    solution = Solution()
    
    nums1 = [0,1,7,4,4,5]
    lower1 = 3
    upper1 = 6
    print(f"Fair pairs {nums1}, [{lower1}, {upper1}]: {solution.countFairPairs(nums1, lower1, upper1)}")
