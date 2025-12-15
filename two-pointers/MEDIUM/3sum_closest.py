# 3Sum Closest
# Problem: https://leetcode.com/problems/3sum-closest/
# Solution:

from typing import List

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        res = sum(nums[:3])
        
        for i in range(len(nums) - 2):
            l, r = i + 1, len(nums) - 1
            
            while l < r:
                cur_sum = nums[i] + nums[l] + nums[r]
                
                if abs(cur_sum - target) < abs(res - target):
                    res = cur_sum
                    
                if cur_sum < target:
                    l += 1
                elif cur_sum > target:
                    r -= 1
                else:
                    return cur_sum
                    
        return res

if __name__ == "__main__":
    solution = Solution()
    
    # Test cases
    nums1 = [-1,2,1,-4]
    target1 = 1
    print(f"Closest sum for {nums1}, target {target1}: {solution.threeSumClosest(nums1, target1)}")
    
    nums2 = [0,0,0]
    target2 = 1
    print(f"Closest sum for {nums2}, target {target2}: {solution.threeSumClosest(nums2, target2)}")
