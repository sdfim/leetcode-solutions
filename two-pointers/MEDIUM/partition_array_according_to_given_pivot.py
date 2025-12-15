# Partition Array According to Given Pivot
# Problem: https://leetcode.com/problems/partition-array-according-to-given-pivot/
# Solution:

from typing import List

class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        left = []
        mid = []
        right = []
        
        for x in nums:
            if x < pivot:
                left.append(x)
            elif x == pivot:
                mid.append(x)
            else:
                right.append(x)
                
        return left + mid + right

if __name__ == "__main__":
    solution = Solution()
    
    nums1 = [9,12,5,10,14,3,10]
    pivot1 = 10
    print(f"Pivoted {nums1} around {pivot1}: {solution.pivotArray(nums1, pivot1)}")
