# Minimize Maximum of Array
# Problem: https://leetcode.com/problems/minimize-maximum-of-array/

from typing import List
import math

class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        # We can increase nums[i-1] and decrease nums[i].
        # This pushes value from right to left.
        # So sum of prefix is constant.
        # max_val in prefix[0...i] >= ceil(sum(nums[0...i]) / (i+1))
        
        curr_sum = 0
        res = 0
        for i, val in enumerate(nums):
            curr_sum += val
            avg = math.ceil(curr_sum / (i + 1))
            res = max(res, avg)
        return res

if __name__ == "__main__":
    solution = Solution()
    print(solution.minimizeArrayValue([3,7,1,6]))  # Output: 5
