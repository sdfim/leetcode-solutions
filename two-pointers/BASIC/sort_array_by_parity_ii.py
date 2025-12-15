# Sort Array By Parity II
# Problem: https://leetcode.com/problems/sort-array-by-parity-ii/
# Solution:

from typing import List

class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        j = 1
        for i in range(0, len(nums), 2):
            if nums[i] % 2 == 1:
                while nums[j] % 2 == 1:
                    j += 2
                nums[i], nums[j] = nums[j], nums[i]
        return nums

if __name__ == "__main__":
    solution = Solution()
    
    nums1 = [4,2,5,7]
    print(f"Sorted by parity II {nums1}: {solution.sortArrayByParityII(nums1)}")
