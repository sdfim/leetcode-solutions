# Merge Sorted Array
# Problem: https://leetcode.com/problems/merge-sorted-array/
# Solution:

from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # Start filling from the end
        p1 = m - 1
        p2 = n - 1
        p = m + n - 1
        
        while p1 >= 0 and p2 >= 0:
            if nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1
            else:
                nums1[p] = nums2[p2]
                p2 -= 1
            p -= 1
            
        # If there are remaining elements in nums2, add them
        # (nums1 elements are already in place)
        while p2 >= 0:
            nums1[p] = nums2[p2]
            p2 -= 1
            p -= 1

if __name__ == "__main__":
    solution = Solution()
    
    # Test cases
    nums1 = [1,2,3,0,0,0]
    m = 3
    nums2 = [2,5,6]
    n = 3
    solution.merge(nums1, m, nums2, n)
    print(f"Merged: {nums1}")
    
    nums1_b = [1]
    m_b = 1
    nums2_b = []
    n_b = 0
    solution.merge(nums1_b, m_b, nums2_b, n_b)
    print(f"Merged: {nums1_b}")
