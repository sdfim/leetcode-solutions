# Find Indices With Index and Value Difference I
# Problem: https://leetcode.com/problems/find-indices-with-index-and-value-difference-i/
# Solution:

from typing import List

class Solution:
    def findIndices(self, nums: List[int], indexDifference: int, valueDifference: int) -> List[int]:
        n = len(nums)
        for i in range(n):
            for j in range(i, n):
                if abs(i - j) >= indexDifference and abs(nums[i] - nums[j]) >= valueDifference:
                    return [i, j]
        return [-1, -1]

if __name__ == "__main__":
    solution = Solution()
    
    nums1 = [5,1,4,1]
    iD1 = 2
    vD1 = 4
    print(f"Indices in {nums1}, iD={iD1}, vD={vD1}: {solution.findIndices(nums1, iD1, vD1)}")
