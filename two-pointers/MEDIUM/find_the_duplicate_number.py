# Find the Duplicate Number
# Problem: https://leetcode.com/problems/find-the-duplicate-number/
# Solution:

from typing import List

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Floyd's Cycle Detection
        slow, fast = nums[0], nums[0]
        
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
                
        slow = nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
            
        return slow

if __name__ == "__main__":
    solution = Solution()
    
    nums1 = [1,3,4,2,2]
    print(f"Duplicate in {nums1}: {solution.findDuplicate(nums1)}")
    
    nums2 = [3,1,3,4,2]
    print(f"Duplicate in {nums2}: {solution.findDuplicate(nums2)}")
