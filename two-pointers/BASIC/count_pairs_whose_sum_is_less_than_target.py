# Count Pairs Whose Sum is Less than Target
# Problem: https://leetcode.com/problems/count-pairs-whose-sum-is-less-than-target/
# Solution:

from typing import List

class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        nums.sort()
        count = 0
        l, r = 0, len(nums) - 1
        
        while l < r:
            if nums[l] + nums[r] < target:
                count += (r - l)
                l += 1
            else:
                r -= 1
                
        return count

if __name__ == "__main__":
    solution = Solution()
    
    nums1 = [-1,1,2,3,1]
    target1 = 2
    print(f"Pairs < {target1} in {nums1}: {solution.countPairs(nums1, target1)}")
    
    nums2 = [-6,2,5,-2,-7,-1,3]
    target2 = -2
    print(f"Pairs < {target2} in {nums2}: {solution.countPairs(nums2, target2)}")
