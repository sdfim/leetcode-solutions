# Find Target Indices After Sorting Array
# Problem: https://leetcode.com/problems/find-target-indices-after-sorting-array/

from typing import List

class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        # O(N log N) sorting
        nums.sort()
        res = []
        for i, num in enumerate(nums):
            if num == target:
                res.append(i)
        return res
        
        # O(N) counting approach also possible, but problem asks "after sorting"
        # and standard sort matches the description perfectly.

if __name__ == "__main__":
    solution = Solution()
    print(solution.targetIndices([1,2,5,2,3], 2))  # Output: [1, 2]
