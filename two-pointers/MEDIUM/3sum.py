# 3Sum
# Problem: https://leetcode.com/problems/3sum/
# Solution:

from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        
        for i in range(len(nums)):
            # Avoid duplicates for the first element
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            left, right = i + 1, len(nums) - 1
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total < 0:
                    left += 1
                elif total > 0:
                    right -= 1
                else:
                    res.append([nums[i], nums[left], nums[right]])
                    left += 1
                    # Avoid duplicates for the second element
                    while nums[left] == nums[left-1] and left < right:
                        left += 1
                        
        return res

if __name__ == "__main__":
    solution = Solution()
    
    # Test cases
    nums1 = [-1,0,1,2,-1,-4]
    print(f"3Sum for {nums1}: {solution.threeSum(nums1)}")
    
    nums2 = [0,1,1]
    print(f"3Sum for {nums2}: {solution.threeSum(nums2)}")
    
    nums3 = [0,0,0]
    print(f"3Sum for {nums3}: {solution.threeSum(nums3)}")
