# 4Sum
# Problem: https://leetcode.com/problems/4sum/
# Solution:

from typing import List

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = []
        quad = []
        
        def kSum(k, start, target):
            if k != 2:
                for i in range(start, len(nums) - k + 1):
                    if i > start and nums[i] == nums[i-1]:
                        continue
                    quad.append(nums[i])
                    kSum(k - 1, i + 1, target - nums[i])
                    quad.pop()
                return

            # Base case: Two Sum II
            l, r = start, len(nums) - 1
            while l < r:
                if nums[l] + nums[r] < target:
                    l += 1
                elif nums[l] + nums[r] > target:
                    r -= 1
                else:
                    res.append(quad + [nums[l], nums[r]])
                    l += 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
                        
        kSum(4, 0, target)
        return res

if __name__ == "__main__":
    solution = Solution()
    
    # Test cases
    nums1 = [1,0,-1,0,-2,2]
    target1 = 0
    print(f"4Sum for {nums1}, target {target1}: {solution.fourSum(nums1, target1)}")
    
    nums2 = [2,2,2,2,2]
    target2 = 8
    print(f"4Sum for {nums2}, target {target2}: {solution.fourSum(nums2, target2)}")
