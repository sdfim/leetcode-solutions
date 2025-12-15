# Two Sum II - Input Array Is Sorted
# Problem: https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1
        
        while l < r:
            s = numbers[l] + numbers[r]
            if s == target:
                return [l + 1, r + 1]
            elif s < target:
                l += 1
            else:
                r -= 1
        
        return []

if __name__ == "__main__":
    solution = Solution()
    print(solution.twoSum([2,7,11,15], 9))  # Output: [1, 2]
