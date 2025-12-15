# Two Sum Less Than K
# Problem: https://leetcode.com/problems/two-sum-less-than-k/
# Solution:

from typing import List

class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        nums.sort()
        res = -1
        l, r = 0, len(nums) - 1
        
        while l < r:
            curr_sum = nums[l] + nums[r]
            if curr_sum < k:
                res = max(res, curr_sum)
                l += 1
            else:
                r -= 1
        return res

if __name__ == "__main__":
    solution = Solution()
    
    nums1 = [34,23,1,24,75,33,54,8]
    k1 = 60
    print(f"Max sum < {k1} in {nums1}: {solution.twoSumLessThanK(nums1, k1)}")
    
    nums2 = [10,20,30]
    k2 = 15
    print(f"Max sum < {k2} in {nums2}: {solution.twoSumLessThanK(nums2, k2)}")
