# Median of Two Sorted Arrays
# Problem: https://leetcode.com/problems/median-of-two-sorted-arrays/

from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Ensure nums1 is smaller for binary search efficiency
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
            
        m, n = len(nums1), len(nums2)
        total_len = m + n
        half_len = (total_len + 1) // 2
        
        left, right = 0, m
        
        while left <= right:
            i = (left + right) // 2
            j = half_len - i
            
            # Constraints:
            # i is size of left part of nums1
            # j is size of left part of nums2
            
            # Check partition validity
            # nums1[i-1] <= nums2[j]
            # nums2[j-1] <= nums1[i]
            
            nums1_left_max = float('-inf') if i == 0 else nums1[i-1]
            nums1_right_min = float('inf') if i == m else nums1[i]
            
            nums2_left_max = float('-inf') if j == 0 else nums2[j-1]
            nums2_right_min = float('inf') if j == n else nums2[j]
            
            if nums1_left_max <= nums2_right_min and nums2_left_max <= nums1_right_min:
                # Correct partition
                if total_len % 2 == 1:
                    return max(nums1_left_max, nums2_left_max)
                else:
                    return (max(nums1_left_max, nums2_left_max) + min(nums1_right_min, nums2_right_min)) / 2.0
            elif nums1_left_max > nums2_right_min:
                # Too far right in nums1
                right = i - 1
            else:
                # Too far left in nums1
                left = i + 1
        
        return 0.0

if __name__ == "__main__":
    solution = Solution()
    print(solution.findMedianSortedArrays([1,3], [2]))  # Output: 2.0
    print(solution.findMedianSortedArrays([1,2], [3,4])) # Output: 2.5
