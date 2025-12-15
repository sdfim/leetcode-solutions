# Number of Distinct Averages
# Problem: https://leetcode.com/problems/number-of-distinct-averages/
# Solution:

from typing import List

class Solution:
    def distinctAverages(self, nums: List[int]) -> int:
        nums.sort()
        averages = set()
        l, r = 0, len(nums) - 1
        
        while l < r:
            avg = (nums[l] + nums[r]) / 2
            averages.add(avg)
            l += 1
            r -= 1
            
        return len(averages)

if __name__ == "__main__":
    solution = Solution()
    
    nums1 = [4,1,4,0,3,5]
    print(f"Distinct averages in {nums1}: {solution.distinctAverages(nums1)}")
    
    nums2 = [1,100]
    print(f"Distinct averages in {nums2}: {solution.distinctAverages(nums2)}")
