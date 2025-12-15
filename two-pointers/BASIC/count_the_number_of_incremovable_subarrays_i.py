# Count the Number of Incremovable Subarrays I
# Problem: https://leetcode.com/problems/count-the-number-of-incremovable-subarrays-i/
# Solution:

from typing import List

class Solution:
    def incremovableSubarrayCount(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        
        for i in range(n):
            for j in range(i, n):
                # Check if removing subarray nums[i:j+1] leaves a strictly increasing array
                is_increasing = True
                last_val = -1
                
                for k in range(n):
                    if k >= i and k <= j:
                        continue
                    if nums[k] <= last_val:
                        is_increasing = False
                        break
                    last_val = nums[k]
                    
                if is_increasing:
                    ans += 1
                    
        return ans

if __name__ == "__main__":
    solution = Solution()
    
    nums1 = [1,2,3,4]
    print(f"Incremovable subarrays in {nums1}: {solution.incremovableSubarrayCount(nums1)}")
    
    nums2 = [6,5,7,8]
    print(f"Incremovable subarrays in {nums2}: {solution.incremovableSubarrayCount(nums2)}")
