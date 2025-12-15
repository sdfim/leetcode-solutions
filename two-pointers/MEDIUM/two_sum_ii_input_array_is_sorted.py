# Two Sum II - Input Array Is Sorted
# Problem: https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
# Solution:

from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """
        Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order,
        find two numbers such that they add up to a specific target number.
        """
        left, right = 0, len(numbers) - 1
        
        while left < right:
            current_sum = numbers[left] + numbers[right]
            
            if current_sum == target:
                return [left + 1, right + 1] # 1-indexed
            elif current_sum < target:
                left += 1
            else:
                right -= 1
                
        return []

if __name__ == "__main__":
    solution = Solution()
    
    # Test cases
    numbers1 = [2,7,11,15]
    target1 = 9
    print(f"Two Sum for {numbers1}, target {target1}: {solution.twoSum(numbers1, target1)}")
    
    numbers2 = [2,3,4]
    target2 = 6
    print(f"Two Sum for {numbers2}, target {target2}: {solution.twoSum(numbers2, target2)}")
