# Squares of a Sorted Array
# Problem: https://leetcode.com/problems/squares-of-a-sorted-array/
# Solution:

from typing import List

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0] * n
        l, r = 0, n - 1
        pos = n - 1
        
        while l <= r:
            l_sq = nums[l] ** 2
            r_sq = nums[r] ** 2
            
            if l_sq > r_sq:
                res[pos] = l_sq
                l += 1
            else:
                res[pos] = r_sq
                r -= 1
            pos -= 1
            
        return res

if __name__ == "__main__":
    solution = Solution()
    
    nums1 = [-4,-1,0,3,10]
    print(f"Sorted squares of {nums1}: {solution.sortedSquares(nums1)}")
    
    nums2 = [-7,-3,2,3,11]
    print(f"Sorted squares of {nums2}: {solution.sortedSquares(nums2)}")
