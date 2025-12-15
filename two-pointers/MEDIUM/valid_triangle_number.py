# Valid Triangle Number
# Problem: https://leetcode.com/problems/valid-triangle-number/
# Solution:

from typing import List

class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        count = 0
        for i in range(len(nums) - 1, 1, -1):
            l, r = 0, i - 1
            while l < r:
                if nums[l] + nums[r] > nums[i]:
                    count += r - l
                    r -= 1
                else:
                    l += 1
        return count

if __name__ == "__main__":
    solution = Solution()
    
    nums1 = [2,2,3,4]
    print(f"Valid triangles in {nums1}: {solution.triangleNumber(nums1)}")
